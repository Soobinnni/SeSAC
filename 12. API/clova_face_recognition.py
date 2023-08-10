import os
import sys
import requests
import cv2
import numpy as np
import json


def clova_face(filename):
    client_id = "gkGXvGKvhCeCUBJGi786" # 개발자센터에서 발급받은 Client ID 값
    client_secret = open("secret.txt", "r").read() # 개발자센터에서 발급받은 Client Secret 값

    url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
    # url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식
    files = {'image': open(filename, 'rb')}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code

    if(rescode==200):
        # print (response.text)
        print ('SUCCESS')
    else:
        print("Error Code:" + rescode)

    data = json.loads(response.text)    
    
    return data

def my_opencv(filename):
    face_info = clova_face(filename)
    # image = cv2.imread(filename)

    img_array = np.fromfile(filename, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    for face in face_info['faces'] :
        roi = face['roi']
        gender = face['gender']['value']

        # 나이, 감정
        age = face['age']['value']
        emotion = face['emotion']['value']

        x, y, w, h = roi['x'],roi['y'],roi['width'],roi['height'] 
        # print(x, y, w, h)

        cv2.rectangle(img, (x,y), (x+w, y+h), (98, 0, 255), 3)
        cv2.putText(img, gender, (x, y+h) , cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 1)
        cv2.putText(img, age, (x, y+(int(h*1.5))) , cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 1)
        cv2.putText(img, emotion, (x, y+(h*2)) , cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 1)



    cv2.imshow('window name', img)
    cv2.waitKey(0)

if __name__ == '__main__' :
    마동석 = 'images/마동석.jpg'
    고윤정 = 'images/고윤정.png'
    한소희 = 'images/한소희.jpg'
    박민영 = 'images/박민영.jpg'
    my_opencv(한소희)