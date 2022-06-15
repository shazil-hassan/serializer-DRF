import requests
import json
URL="http://127.0.0.1:8000/stucreate/"
data={
    'name':'kazmi',
    'email':'kazmi@gmail.com',
    'phone':'0303030021',
    'age':21
}
json_data=json.dumps(data)
r=requests.post(url=URL,data=json_data)
data=r.json()




URL="http://127.0.0.1:8000/stuupdate/"
data={
'id':6,
'name':'murshad',
'email':'murshad@gmail.com',
'phone':'03324996332',
}
json_data=json.dumps(data)
r=requests.put(url=URL,data=json_data)
data=r.json()
print(data)



URL="http://127.0.0.1:8000/studelete/"
data={'id':6}

json_data=json.dumps(data)

r=requests.delete(url = URL, data = json_data)
data=r.json()
print(data)