import pyttsx3 as pt
#name=input("enter your name: ")
engine = pt.init()
file = open("test.txt")
fsp=file.readline()
engine.say(fsp)
#engine.say("hello "+ name)
#rate=engine.setProperty("rate",100)
#vol=engine.setProperty("volume",1)
engine.runAndWait()
engine.stop()