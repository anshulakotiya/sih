import cv2
import numpy as np
facecetect= cv2.CascadeClassifier('D:\PROGRAMES FILES\Anaconda3\Library\etc\haarcascades\haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0);
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=facecetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("face",img);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()