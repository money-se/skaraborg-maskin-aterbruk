import {createClient} from "npm:@supabase/supabase-js@2";
const ORIGIN="https://skaraborgmaskin.se",AD="271abfdc-76f8-46e8-be35-2a2d11ecdd35";
const headers={"Access-Control-Allow-Origin":ORIGIN,"Access-Control-Allow-Headers":"content-type,apikey","Access-Control-Allow-Methods":"POST, OPTIONS","Content-Type":"application/json","Cache-Control":"no-store"};
const respond=(status:number,obj:unknown)=>new Response(JSON.stringify(obj),{status,headers});
async function hash(s:string){const a=await crypto.subtle.digest("SHA-256",new TextEncoder().encode(s));return [...new Uint8Array(a)].map(x=>x.toString(16).padStart(2,"0")).join("")}
Deno.serve(async request=>{
 if(request.method==="OPTIONS")return new Response(null,{headers});
 if(request.method!=="POST")return respond(405,{error:"Method"});
 if(request.headers.get("origin")!==ORIGIN)return respond(403,{error:"Origin"});
 const secret=Deno.env.get("TURNSTILE_SECRET_KEY"),pepper=Deno.env.get("MESSAGE_PEPPER"),key=Deno.env.get("SUPABASE_SERVICE_ROLE_KEY"),url=Deno.env.get("SUPABASE_URL");
 if(!secret||!pepper||pepper.length<24||!key||!url)return respond(503,{error:"Not configured"});
 if(Number(request.headers.get("content-length")||0)>9000)return respond(413,{error:"Size"});
 let data:any;try{data=await request.json()}catch{return respond(400,{error:"Format"})}
 if(!data||(data.action!=="read"&&(typeof data.captcha!=="string"||data.captcha.length>4096||data.captcha.length<1)))return respond(400,{error:"Captcha"});
 if(data.action!=="read"){const verification=await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify",{method:"POST",headers:{"content-type":"application/x-www-form-urlencoded"},body:new URLSearchParams({secret,response:data.captcha})}).then(r=>r.ok?r.json():null).catch(()=>null);
 if(!verification?.success||verification.hostname!=="skaraborgmaskin.se")return respond(403,{error:"Captcha"});}
 const db=createClient(url,key,{auth:{persistSession:false,autoRefreshToken:false}});
 const limit=await db.rpc("ad_message_rate_check",{p_hash:await hash(pepper+":test-messages-total:"+(data.action==="read"?"read":"write")),p_limit:data.action==="read"?360:20,p_window_minutes:60});
 if(limit.error||limit.data!==true)return respond(429,{error:"Rate limit"});
 if(data.action==="new"){
  const name=typeof data.name==="string"?data.name.trim():"",email=typeof data.email==="string"?data.email.trim().toLowerCase():"",body=typeof data.message==="string"?data.message.trim():"";
  if(name.length<1||name.length>120||email.length>254||!/^\S+@\S+\.\S+$/.test(email)||body.length<1||body.length>3000)return respond(400,{error:"Fields"});
  const perEmail=await db.rpc("ad_message_rate_check",{p_hash:await hash(pepper+":test-email:"+email),p_limit:3,p_window_minutes:1440});
  if(perEmail.error||perEmail.data!==true)return respond(429,{error:"Rate limit"});
  const token=crypto.randomUUID()+"-"+crypto.randomUUID();
  const conversation=await db.from("ad_conversations").insert({ad_id:AD,customer_name:name,customer_email:email,access_token_hash:await hash(pepper+":test-token:"+token)}).select("id").single();
  if(conversation.error)return respond(500,{error:"Not available"});
  const m=await db.from("ad_messages").insert({conversation_id:conversation.data.id,sender:"customer",body});
  if(m.error){await db.from("ad_conversations").delete().eq("id",conversation.data.id);return respond(500,{error:"Failed"})}
  return respond(201,{id:conversation.data.id,token});
 }
 const id=typeof data.id==="string"?data.id:"",token=typeof data.token==="string"?data.token:"";
 if(!/^[0-9a-f-]{36}$/i.test(id)||!/^[-0-9a-f]{73}$/i.test(token))return respond(400,{error:"Credentials"});
 const conv=await db.from("ad_conversations").select("id,status").eq("ad_id",AD).eq("id",id).eq("access_token_hash",await hash(pepper+":test-token:"+token)).maybeSingle();
 if(conv.error||!conv.data)return respond(404,{error:"Not found"});
 if(conv.data.status!=="open")return respond(410,{error:"Closed"});
 if(data.action==="read"){
  const threadLimit=await db.rpc("ad_message_rate_check",{p_hash:await hash(pepper+":test-read:"+id),p_limit:120,p_window_minutes:60});if(threadLimit.error||threadLimit.data!==true)return respond(429,{error:"Rate limit"});
  const messages=await db.from("ad_messages").select("sender,body,sent_at").eq("conversation_id",id).order("sent_at").limit(100);
  return messages.error?respond(500,{error:"Failed"}):respond(200,{messages:messages.data});
 }
 if(data.action==="reply"){
  const body=typeof data.message==="string"?data.message.trim():"";
  if(body.length<1||body.length>3000)return respond(400,{error:"Message"});
  const write=await db.from("ad_messages").insert({conversation_id:id,sender:"customer",body});
  return write.error?respond(500,{error:"Failed"}):respond(201,{ok:true});
 }
 return respond(400,{error:"Action"});
});