import requests

roomId="Y2lzY29zcGFyazovL3VzL1JPT00vMjlhNmVkOWYtZTE2OC0zYzJmLTg1ZGItNTRmZWViNzEyYzVj"
token='NTVkODBiZjctMzg5YS00ZDI0LTlmODgtZWI5MzY4OTkyZTc5NTBjOThiMDUtOGQy_PF84_consumer'

url="https://api.ciscospark.com/v1/messages?roomId=" + roomId
header = {"content-type": "application/json; charset=utf-8", "authorization":"Bearer "+token}
response=requests.get(url, headers = header, verify = True)

print(response.json())
