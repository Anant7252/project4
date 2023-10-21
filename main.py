import kivy
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang.builder import Builder





class Newapp(MDApp):
 
    def build(self):
        # background='red'
        return Builder.load_file("new.kv")
    
    def say_hello(self):
        hello_label=self.root.ids.hello_label
        hello_label.text="hello anant"


if __name__=='__main__':
    Newapp().run()
