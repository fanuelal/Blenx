from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.icon_definitions import md_icons
from kivy.uix.screenmanager import ScreenManager, Screen
class Loginscreen(Screen):
    pass
class Regscreen(Screen):
    pass
class WindowManager(ScreenManager):
    pass
class Blenx(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('login.kv')
if __name__ == '__main__':
    Blenx().run()
