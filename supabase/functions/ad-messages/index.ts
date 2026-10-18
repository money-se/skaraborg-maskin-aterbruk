// Customer message gateway - fail closed until secrets are installed.
// Required Supabase function secrets: TURNSTILE_SECRET_KEY, MESSAGE_PEPPER.
// Required project secrets: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY (server-side only).
import { createClient } from "npm:@supabase/supabase-js@2";
const cors = {"Access-Control-Allow-Origin":"https://skaraborgmaskin.se","Access-Control-Allow-Headers":"content-type,apikey,x-client-info","Access-Control-Allow-Methods":"POST, OPTIONS","Content-Type":"application/json"};
const reply=(status:number,body:unknown)=>new Response(JSON.stringify(body),{status,headers:cors});
const encoder=new TextEncoder();
async function digest(value:string){const buffer=await crypto.subtle.digest("SHA-256",encoder.encode(value));return [...new Uint8Array(buffer)].map(x=>x.toString(16).padStart(2,"0")).join("")}
function normalized(s:unknown,max:number){return typeof s==="string"&&s.trim().length>0&&s.trim().length<=max?s.trim():null}
async function captcha(token:string,secret:string){const response=await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify",{method:"POST",headers:{"content-type":"application/x-www-form-urlencoded"},body:new URLSearchParams({secret,response:token})});if(!response.ok)return false;const data=await response.json();return data.success===true&&data.hostname==="skaraborgmaskin.se"}
Deno.serve(async req=>{
 if(req.method==="OPTIONS")return new Response(null,{headers:cors});
 if(req.method!=="POST")return reply(405,{error:"Method not allowed"});
 const expectedOrigin="https://skaraborgmaskin.se";
 if(req.headers.get("origin")!==expectedOrigin)return reply(403,{error:"Invalid origin"});
 const secret=Deno.env.get("TURNSTILE_SECRET_KEY");
 const pepper=Deno.env.get("MESSAGE_PEPPER");
 const key=Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");
 const url=Deno.env.get("SUPABASE_URL");
 if(!secret||!pepper||pepper.length<24||!key||!url)return reply(503,{error:"Messaging not configured"});
 if(Number(req.headers.get("content-length")||"0")>12000)return reply(413,{error:"Message too large"});
 let data:any;try{data=await req.json()}catch{return reply(400,{error:"Bad JSON"})}
 const action=normalized(data.action,16);
 if(!["new","read","reply"].includes(action||""))return reply(400,{error:"Invalid action"});
 if(action!=="read"){const turnstile=normalized(data.captcha,4096);if(!turnstile)return reply(400,{error:"Verification required"});try{if(!await captcha(turnstile,secret))return reply(403,{error:"Verification failed"})}catch{return reply(503,{error:"Verification unavailable"})}}
 const db=createClient(url,key,{auth:{persistSession:false,autoRefreshToken:false}});
 // Never trust client-controlled forwarding headers as IP identity.
 // A shared global bucket limits total load; additional email and thread buckets apply below.
 const globalHash=await digest(pepper+":global:ad-messages");
 const rate=await db.rpc("ad_message_rate_check",{p_hash:globalHash,p_limit:300,p_window_minutes:60});
 if(rate.error||rate.data!==true)return reply(429,{error:"Too many requests"});
 if(action==="new"){
   if(data.website)return reply(200,{ok:true}); // honeypot
   const adId=normalized(data.ad_id,80),name=normalized(data.name,120),email=normalized(data.email,254),body=normalized(data.message,3000);
   if(!adId||!/^[a-f0-9-]{36}$/i.test(adId)||!name||!email||!body||!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))return reply(400,{error:"Invalid fields"});
   const emailHash=await digest(pepper+":email:"+email.toLowerCase());
   const limiter=await db.rpc("ad_message_rate_check",{p_hash:emailHash,p_limit:4,p_window_minutes:1440});
   if(limiter.error||limiter.data!==true)return reply(429,{error:"Too many requests"});
   const ad=await db.from("ads").select("id,status,published").eq("id",adId).eq("published",true).eq("status","sale").maybeSingle();
   if(ad.error||!ad.data)return reply(404,{error:"Ad not available"});
   const token=crypto.randomUUID()+"-"+crypto.randomUUID();const hash=await digest(pepper+":token:"+token);
   const conv=await db.from("ad_conversations").insert({ad_id:adId,customer_name:name,customer_email:email,access_token_hash:hash}).select("id").single();
   if(conv.error)return reply(500,{error:"Could not open conversation"});
   const msg=await db.from("ad_messages").insert({conversation_id:conv.data.id,sender:"customer",body});
   if(msg.error){await db.from("ad_conversations").delete().eq("id",conv.data.id);return reply(500,{error:"Could not send message"})}
   return reply(201,{conversation_id:conv.data.id,token});
 }
 const id=normalized(data.conversation_id,80),token=normalized(data.token,200);
 if(!id||!/^[a-f0-9-]{36}$/i.test(id)||!token||!/^[-a-f0-9]{73}$/i.test(token))return reply(400,{error:"Missing conversation credentials"});
 const hash=await digest(pepper+":token:"+token);
 const threadBucket=await db.rpc("ad_message_rate_check",{p_hash:await digest(pepper+":thread:"+id+":"+action),p_limit:action==="read"?180:20,p_window_minutes:60});
 if(threadBucket.error||threadBucket.data!==true)return reply(429,{error:"Too many requests"});
 const conv=await db.from("ad_conversations").select("id,status,customer_name").eq("id",id).eq("access_token_hash",hash).maybeSingle();
 if(conv.error||!conv.data)return reply(404,{error:"Conversation unavailable"});
 if(conv.data.status!=="open")return reply(410,{error:"Conversation closed"});
 if(action==="read"){
   const messages=await db.from("ad_messages").select("sender,body,sent_at").eq("conversation_id",id).order("sent_at",{ascending:true}).limit(500);
   if(messages.error)return reply(500,{error:"Could not read messages"});
   return reply(200,{messages:messages.data});
 }
 const body=normalized(data.message,3000);if(!body)return reply(400,{error:"Message required"});
 const res=await db.from("ad_messages").insert({conversation_id:id,sender:"customer",body});
 if(res.error)return reply(500,{error:"Could not send message"});
 return reply(201,{ok:true});
});
