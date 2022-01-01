import cv2
#from settings import BASE_DIR
import numpy as np
facecetect= cv2.CascadeClassifier("D:\\PROGRAMES FILES\\Anaconda3\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml")
cam=cv2.VideoCapture(0);
id= int(input("enter the id"))
sampleNum=0;
while(True):
    ret, img = cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=facecetect.detectMultiScale(gray,1.3,5);
    for(x, y, w, h) in faces:
        sampleNum = sampleNum+1;
        cv2.imwrite('user.'+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
        cv2.waitKey(100);
    cv2.imshow("face", img);
    cv2.waitKey(1);
    if(sampleNum>19):
        break;
cam.release()
cv2.destroyAllWindows()