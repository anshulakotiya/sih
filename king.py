import cv2
import numpy as np
import PIL

facedetect=cv2.CascadeClassifier('D:\PROGRAMES FILES\Anaconda3\Library\etc\haarcascades\haarcascade_frontalface_default.xml')
cam= cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read('D:\\new\\hello\\hello\\softteam\\recognizer\\trainingdata.yml')
id=0
fontface=cv2.FONT_HERSHEY_SIMPLEX
while (True):
         ret,img=cam.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=facedetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]

        img,conf=ret(roi_gray)
        if conf>=100:
            print(id)
            font=cv2.FONT_HERSHEY_COMPLEX
            NAME=id
            color=(0,0,0)
            stroke=2
            cv2.putText(img,NAME,(x,y),1,color,stroke,cv2.LINE_AA)

        cv2.imwrite(img,roi_color)
        color=(0,0,0)
        stroke=2
        end_cord_x=x+w
        end_cord_y=y+h
        cv2.rectangle(img,(x,y),(end_cord_x,end_cord_y),color,stroke)

    cv2.imshow("frame",img)

    cam.release()
    cv2.destroyAllWindows()