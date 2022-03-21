import cv2
import numpy as np
#attendance writer
def writingOnFile():
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
fd=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam =cv2.VideoCapture(0)
dataList= open("lists.csv","a")
id = input('Enter ID: ')
customer_name = input('Enter full Name: ')
redChecker(id,customer_name)
sampleNum=0
counter = 0
readyMaker = 0
sample_counter =0
print("I am learning your face please rotate your face in different angles")
while(True):
    re,img=cam.read()
    cv2.imshow("Trying to recognized you",img)
    readyMaker = readyMaker + 1
    if (readyMaker <=1):
        cv2.putText(img,"READY",(100,100),cv2.FONT_HERSHEY_TRIPLEX,4,(0,255,0),4)
        for counter in range(3):
            cv2.putText(img,f'{int(counter+1)}',(300,300),cv2.FONT_HERSHEY_COMPLEX,4,(100,100,150),4)
            re,img=cam.read()
            cv2.imshow("Trying to recognized you",img)
            cv2.waitKey(3000)
    #print for read
    #cv2.putText(img,f'{int(x+1)} %',(300,300),cv2.FONT_HERSHEY_COMPLEX,4,(100,100,150),4)

    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=fd.detectMultiScale(gray,1.3,1)
    for(x,y,w,h) in faces:
        sample_counter += 1
        cv2.imwrite("data/"+str(customer_name)+"_"+str(id)+"_"+str(sampleNum)+".jpg",gray[y:y+h, x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(1)
    cv2.imshow("Trying to recognized you",img)
    cv2.waitKey(10)   
    k = cv2.waitKey(30) & 0xff
    if (sample_counter == 100):
        break
    elif(cv2.waitKey(1)==ord('q')):
        break
    elif k==27:
        break
writingOnFile()
print("finished learning")
cam.release()
cv2.destroyAllWindows()
