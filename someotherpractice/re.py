import requests
method ='post'

url="https://app.adjust.com/session"

data={
"android_uuid":"73e3844e-ceab-42d6-86ab-f9afbffda493",
"api_level":"27",
"app_token":"dsieoyelsgzk",
"app_version":"2.12.3",
"attribution_deeplink":"1",
"connectivity_type":"1",
"country":"US",
"cpu_type":"armeabi-v7a",
"created_at":"2023-10-25T12:15:24.895Z+0530",
"device_manufacturer":"motorola",
"device_name":"Moto G (5) Plus",
"device_type":"phone",
"display_height":"1776",
"display_width":"1080",
"environment":"production",
"event_buffering_enabled":"0",
"gps_adid":"b2ba3d40-304c-4d2e-a2c9-c6966ad8d41f",
"gps_adid_attempt":"1",
"gps_adid_src":"service",
"hardware_name":"OPS28.85-17-6-2",
"installed_at":"2023-10-25T12:07:21.000Z+0530",
"language":"en",
"needs_response_details":"1",
"os_build":"OPS28.85-17-6-2",
"os_name":"android",
"os_version":"8.1.0",
"package_name":"com.todtv.tod",
"screen_density":"high",
"screen_format":"normal",
"screen_size":"normal",
"sent_at":"2023-10-25T12:15:25.119Z+0530",
"session_count":"1",
"tracking_enabled":"1",
"ui_mode":"1",
"updated_at"	:"2023-10-25T12:07:21.000Z+0530"
}
params=None

headers={
"Client-SDK":"android4.31.0",
 
"Content-Type":"application/x-www-form-urlencoded",
"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 8.1.0; Moto G (5) Plus Build/OPS28.85-17-6-2)",
 
 
"Accept-Encoding":"gzip",
 


}

res=requests.post(url,data=data,params=params,headers=headers)
print(res.status_code)