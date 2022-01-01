from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import detail_of_worker, photo,attends
import os
import cv2
import numpy as np
from PIL import Image
import datetime
#
def photos(request):
    return render(request, 'face_capture.html')

def account_verify(request):
    app = request.POST.get('appli_no')
    global appli
    appli = app
    previous = detail_of_worker.objects.get(ap_no_worker=appli)
    return render(request, 'photo_verification.html', {'data': previous})

def capture(request):
    check = request.POST.get('true', 'off')
    if check == 'on':
        id = appli
        worker_app_no = id
        all_details = photo(worker_app_no=worker_app_no)
        all_details.save()
        facecetect = cv2.CascadeClassifier('D:\PROGRAMES FILES\Anaconda3\Library\etc\haarcascades\haarcascade_frontalface_default.xml')
        cam = cv2.VideoCapture(0)
        sampleNum = 0
        while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = facecetect.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    sampleNum = sampleNum + 1
                    cv2.imwrite('D:\\new\\hello\\hello\\softteam\\dataset\\' + str(id) + "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
                    cv2.waitKey(100)
                cv2.imshow("face", img)
                cv2.waitKey(1)
                if (sampleNum > 101):
                    break
        cam.release()
        cv2.destroyAllWindows()
        #train
        reco = cv2.face.LBPHFaceRecognizer_create()
        path = "D:\\new\\hello\\hello\\softteam\\dataset"

        def getImagesWithID(path):
            imagepaths = [os.path.join(path, f) for f in os.listdir(path)]
            faces = []
            IDs = []
            for imagepath in imagepaths:
                faceimg = Image.open(imagepath).convert('L');
                facenp = np.array(faceimg, 'uint8')
                ID = int(os.path.split(imagepath)[-1].split('.')[1])
                faces.append(facenp)
                IDs.append(ID)
                cv2.imshow("training", facenp)
                cv2.waitKey(10)
            return np.array(IDs), faces

        Ids, faces = getImagesWithID(path)
        reco.train(faces, Ids)
        reco.save("D:\\new\\hello\\hello\\softteam\\recognizer/trainingdata.yml")
        cv2.destroyAllWindows()

        return HttpResponse("captured and trained")


def faceverify(request):
    faceDetect = cv2.CascadeClassifier(
        'D:\PROGRAMES FILES\Anaconda3\Library\etc\haarcascades\haarcascade_frontalface_default.xml');
    cam = cv2.VideoCapture(0);
    rec = cv2.face.LBPHFaceRecognizer_create();
    rec.read("D:\\new\\hello\\hello\\softteam\\recognizer\\trainingdata.yml")

    id = 0
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, conf = rec.predict(gray[y:y + h, x:x + w])
            if (id == 10002):
                an = "anugrah"
                print(an)
            cv2.putText(img, str(id), (x, y + h), fontface, 2, (255, 0, 0), 3)
        cv2.imshow("Face", img);
        if (cv2.waitKey(1) == ord('q')):
            break;
    cam.release()
    cv2.destroyAllWindows()
    return HttpResponse('detected')