import requests
import json

url="https://www.sarkariresult.com/"

data= {
"hello":"hello"

}

params=None

headers={

}

res=requests.get(url,data=json.dumps(data),params=params,headers=headers)
hel=json.loads(res.data)
print(hel)