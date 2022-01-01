import os
import cv2
import numpy as np
from PIL import Image

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
