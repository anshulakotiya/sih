from django.shortcuts import redirect
import cv2
import numpy as np

faceDetect=cv2.CascadeClassifier('D:\PROGRAMES FILES\Anaconda3\Library\etc\haarcascades\haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
rec=cv2.face.LBPHFaceRecognizer_create();
rec.read("D:\\new\\hello\\hello\\softteam\\recognizer\\trainingdata.yml")

id=0
fontface=cv2.FONT_HERSHEY_SIMPLEX
userid=0
while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if conf<15:
            print(id)
            userid = id
            cv2.putText(img,'detected',(x,y,h),2,(0,255,0),2)
        else:
            cv2.putText(img, "Unknown",(x,y+h), 2, (0,0,255),2)
    cv2.imshow("Face",img)
    if(cv2.waitKey(1)==ord('q')):
        break
    elif(id != 0):
        cv2.waitKey(1000)
        cam.release()
        cv2.destroyAllWindows()
        print(1)
cam.release()
cv2.destroyAllWindows()