import os
import cv2
import numpy as np
from PIL import Image
recognizer = cv2.face.LBPHFaceRecognizer_create()
path="data"
def getImagesWithId(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    Names=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('_')[1])
        Names=(os.path.split(imagePath)[-1].split('_')[0])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("I am teaching my self",faceNp)
        cv2.waitKey(10)
    return IDs,faces,Names

IDs,faces,Names=getImagesWithId(path)
recognizer.train(faces,np.array(IDs))
recognizer.save('recognized/trainningData.yml')
exit()
#os.cd(path)
#os.del(*.*)
cv2.destroyAllWindows()
