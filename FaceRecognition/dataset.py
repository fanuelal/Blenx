#importing necessary packages
import cv2
import numpy as np
import json
import subprocess
#attendance writer
def writingOnFile(ids,name):
    dict={'name':name, 'id':ids}
    json_dict = json.dumps(dict, indent=4)
    with open("list.json","r") as ofile:
        readenFile = json.load(ofile)
    readenFile.append(dict)
    with open("list.json","r") as ofile:
        readenFile = json.load(ofile)
    readenFile.append(dict)
    with open("list.json","w") as filewriter:
        json.dump(readenFile, filewriter, indent=4)
    dataList.write(customer_name+","+id)
    dataList.close()
#attendance checker 
def redChecker(name,user_id):
    file_reader = open("lists.csv","r")
    for x in file_reader:
        savedName = x.split(',')[0]
        savedId = x.split(',')[1]
        if (savedName == name or user_id == savedId):
            print("This name or Id  is taken")
            costemer_name = input("Enter again your correct name")
            id = input('Enter ID: ')
#initialize the global variables
fd=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam =cv2.VideoCapture(0)
dataList= open("lists.csv","a")
id = input('Enter ID: ')
customer_name = input('Enter full Name: ')
sampleNum=0
counter = 0
readyMaker = 0
sample_counter =0
redChecker(id,customer_name)
print("I am learning your face please rotate your face in different angles")
while(True):
    re,img=cam.read()
    cv2.imshow("Trying to recognized you",img)
    #convert the image from bgr ti gray
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=fd.detectMultiScale(gray,1.25,minNeighbors=4, minSize=(40, 40),flags=cv2.CASCADE_SCALE_IMAGE)
    #face cordinate extraction
    for(x,y,w,h) in faces:
        print('w: '+str(w)+' h:'+str(h))
        sample_counter += 1
        cv2.imwrite("data/"+str(customer_name)+"_"+str(id)+"_"+str(sample_counter)+".jpg",gray[y:y+h, x:x+w])
        print("file have been righten")
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(1)
    #the images to 
    cv2.imshow("Trying to recognized you",img)
    cv2.waitKey(10)   
    print(sample_counter)
    k = cv2.waitKey(30) & 0xff
    if (sample_counter >= 200):
        break
    elif(cv2.waitKey(1)==ord('q')):
        break
writingOnFile(id,customer_name)
print("finished capturing")
cmdtrainer = 'python train.py'
cmddetector = 'python detector.py'
trainer = subprocess.Popen(cmdtrainer, shell=True)
checking = input('Are you ready to check: ')
detect = subprocess.Popen(cmddetector, shell=True)
cam.release()
cv2.destroyAllWindows() 
