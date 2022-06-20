import cv2
import numpy as np
import os
from PIL import Image
import json
#imported packages


#basic variables initializations that we use for detection 
fd=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognized\\trainningData.yml")
fontScale = 1/2
fontFace = cv2.FONT_HERSHEY_COMPLEX


ret, img = cam.read()
Ids=0
#infinite loop for taking an image continous ly
while (True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    #converted to gray scale image
    faces = fd.detectMultiScale(gray,1.4,minNeighbors=4, minSize=(40, 40),flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        #loop for creating the box around the face
        rectcolor = (0,0,255)
        #initialize the rectangle color
        fontColor = (255, 255, 255)
        locy = ((y+h+35)-15) # the text location will be in the middle
        locx = (x+50)
        Ids,conf=recognizer.predict(gray[y:y+h,x:x+w])
        #print(conf)
        owner = 'Unknown'
        #checks if the face is similar or not
        with open("list.json", 'r') as readen:
            name_json = json.load(readen)
        for value in name_json:
            if str(Ids) == value['id']:
                owner = value['name']
        if conf < 67:
            #IDs,faces=getImagesWithId(path)
            print(conf)
            rectcolor = (0,255,0)
            name = owner
        else:
            name='unkown'
            Ids = ''
            print(conf)
        #draws rectangle for each images
        cv2.rectangle(img,(x,y),(x+w,y+h),rectcolor,1)
        cv2.rectangle(img, (x,(y+h)+35),(x+w,y+h),rectcolor,cv2.FILLED)
        cv2.putText(img,name.upper(),(locx,locy),fontFace,fontScale,fontColor,2)
    cv2.imshow("BlenX",img)
    if(cv2.waitKey(1)==ord('q')):
        #the program quit for pressing the q button
                break
print("End of programm")
cam.release()
cv2.destroyAllWindows()
