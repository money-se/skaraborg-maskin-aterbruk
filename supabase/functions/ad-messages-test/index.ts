// Private diagnostic endpoint. JWT required at gateway AND checked here.
// No customer captcha bypass is exposed by the public ad-messages endpoint.
import {createClient} from "npm:@supabase/supabase-js@2";
const url=Deno.env.get("SUPABASE_URL")||"",service=Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")||"",pub=Deno.env.get("SUPABASE_ANON_KEY")||"";
const headers={"Content-Type":"application/json","Cache-Control":"no-store","Access-Control-Allow-Origin":"*","Access-Control-Allow-Headers":"authorization,apikey,content-type,x-client-info"};
function result(code:number,data:unknown){return new Response(JSON.stringify(data),{status:code,headers})}
Deno.serve(async req=>{
 if(req.method==="OPTIONS")return new Response(null,{headers});
 if(req.method!=="POST")return result(405,{error:"Method not allowed"});
 if(!url||!service||!pub)return result(503,{error:"Service configuration missing"});
 const bearer=req.headers.get("authorization")||"";
 if(!bearer.startsWith("Bearer "))return result(401,{error:"Login required"});
 const userClient=createClient(url,pub,{global:{headers:{Authorization:bearer}},auth:{persistSession:false,autoRefreshToken:false}});
 const userResult=await userClient.auth.getUser(bearer.slice(7));
 if(userResult.error||!userResult.data.user)return result(401,{error:"Invalid session"});
 const db=createClient(url,service,{auth:{persistSession:false,autoRefreshToken:false}});
 const uid=userResult.data.user.id;
 const membership=await db.from("ad_editors").select("user_id").eq("user_id",uid).maybeSingle();
 if(membership.error||!membership.data)return result(403,{error:"Editor permission required"});
 const marker="TEST KONVERSATION (RADERA)";
 let body:any;try{body=await req.json()}catch{return result(400,{error:"Bad JSON"})}
 if(body.action==="create"){
   const count=await db.from("ads").select("id",{count:"exact",head:true}).eq("created_by",uid).eq("title",marker).neq("status","sold");
   if(count.error||count.count===null)return result(500,{error:"Cannot check test limit"});
   if(count.count>=2)return result(429,{error:"Too many active test ads"});
   const ad=await db.from("ads").insert({created_by:uid,title:marker,description:"Endast intern testannons. Publiceras inte.",price_sek:1,status:"sale",published:false}).select("id").single();
   if(ad.error)return result(500,{error:"Could not create test ad"});
   const c=await db.from("ad_conversations").insert({ad_id:ad.data.id,customer_name:"Testkund",customer_email:"test@example.invalid",access_token_hash:crypto.randomUUID()}).select("id").single();
   if(c.error){await db.from("ads").delete().eq("id",ad.data.id);return result(500,{error:"Could not create thread"})}
   const m=await db.from("ad_messages").insert({conversation_id:c.data.id,sender:"customer",body:"Hej! Detta är ett testmeddelande. Kan ni svara?"});
   if(m.error){await db.from("ads").delete().eq("id",ad.data.id);return result(500,{error:"Could not create test message"})}
   return result(201,{ad_id:ad.data.id,conversation_id:c.data.id,notice:"Open inbox, reply, then choose cleanup"});
 }
 if(body.action==="cleanup"){
   const adId=typeof body.ad_id==="string"&&/^[0-9a-f-]{36}$/i.test(body.ad_id)?body.ad_id:"";
   if(!adId)return result(400,{error:"Invalid test ID"});
   const found=await db.from("ads").select("id").eq("id",adId).eq("created_by",uid).eq("title",marker).eq("published",false).maybeSingle();
   if(found.error||!found.data)return result(404,{error:"Test ad not found"});
   const sold=await db.from("ads").update({status:"sold"}).eq("id",adId).select("id").single();
   if(sold.error)return result(500,{error:"Could not mark sold"});
   const remaining=await db.from("ad_conversations").select("id",{count:"exact",head:true}).eq("ad_id",adId);
   if(remaining.error||remaining.count!==0)return result(500,{error:"Messages may remain after sale"});
   const removed=await db.from("ads").delete().eq("id",adId);
   if(removed.error)return result(500,{error:"Sold; but cleanup of test advertisement failed"});
   return result(200,{ok:true,conversations_remaining:0,test_ad_removed:true});
 }
 return result(400,{error:"Unknown action"});
});
