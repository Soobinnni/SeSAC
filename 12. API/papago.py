import os
import sys
import urllib.request
import json

client_id = "gkGXvGKvhCeCUBJGi786" # 개발자센터에서 발급받은 Client ID 값
client_secret = open("secret.txt", "r").read() # 개발자센터에서 발급받은 Client Secret 값

encText = urllib.parse.quote("반갑습니다")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    data = json.loads(response_body)
    print(data['message']['result']['translatedText'])
else:
    print("Error Code:" + rescode)