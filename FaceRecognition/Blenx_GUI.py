#pakages that are needed 
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.icon_definitions import md_icons
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import kivy 
import cv2
import numpy as np
import os
#version of the software
kivy.require('1.0.0')

fd=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #frontal face cascade file 
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognized\\trainningData.yml") #the trained data storing path
fontScale = 1/2 #give the font scale by half
fontFace = cv2.FONT_HERSHEY_COMPLEX
Ids=0

class ExamHall(MDApp):
    #The class of examhall that the student will get after login

    def build(self):
        #function for creating the exam layout for student
        Layout = MDBoxLayout(orientation='vertical',
        spacing=10) 
        self.image = Image()
        Layout.add_widget(self.image)

        Layout.add_widget(MDRaisedButton(
            text="Submit",
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(None,None)
        ))
        self.cam = cv2.VideoCapture(0)
        Clock.schedule_interval(self.loadVideo, 1.0/30.0)
        ret, frames = self.cam.read()
        gray=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY) 
        #converting live cam image to gray 
        faces = fd.detectMultiScale(gray,1.3,5)
        #loop for detecting the the 4 sides around the face
        for(x,y,w,h) in faces:
            name='unkown'
            #initializing the name to unknown
            Ids,conf=recognizer.predict(gray[y:y+h,x:x+w])
            print(conf)
            if conf<55:
                #IDs,faces=getImagesWithId(path)
                print(Ids)
                rectcolor = (0,255,0)
                name = 'Fanuel' 
                print(name)
            else:
                name = 'unknown'
                print(name)
        return Layout
    def loadVideo(self, *args):
        #this function gone to start the img reading 
        ret, frames = self.cam.read()
        self.image_frame = frames
        buffer = cv2.flip(frames, 0).tostring()
        texture = Texture.create(size=(frames.shape[1], frames.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt="ubyte")
        self.image.texture = texture

            

class Loginscreen(Screen):
    #the class to login screen designed on the screens,kv file
    pass
class Regscreen(Screen):
    #this class is also for the regestration purpoa designed 
    pass
class Examscreen(Screen):
    #exam class with screen parameter with exam caller function
    def examcaller(self):
        #exam caller cals the Exam hall 
        ExamHall().run()
        return Builder.load_file('Examhall.kv')
   
class WindowManager(ScreenManager):
    #this will manages for the above class
    pass

class Blenx(MDApp):
    #This is the main or root class for this program
    def build(self):
        #this method defines the theme style and returns the kv file path
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('Screens.kv')

if __name__ == '__main__':
    Blenx().run()
