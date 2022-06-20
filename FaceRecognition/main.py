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
import main
#from PIL import Image
kivy.require('1.0.0')

class ExamHall(MDApp):
    #fd=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    def build(self):
        Layout = MDBoxLayout(orientation='vertical') 
        self.image = Image()
        Layout.add_widget(self.image)
        Layout.add_widget(MDRaisedButton(
            text="Click Here",
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(None,None)
        ))
        self.cam = cv2.VideoCapture(0)
        Clock.schedule_interval(self.loadVideo, 1.0/30.0)
        return Layout
    def loadVideo(self, *args):
        ret, frames = self.cam.read()
        self.image_frame = frames
        buffer = cv2.flip(frames, 0).tostring()
        texture = Texture.create(size=(frames.shape[1], frames.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt="ubyte")
        self.image.texture = texture
if __name__ == '__main__':
    ExamHall().run()
