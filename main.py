from kivy.app import App
from kivy.uix.label import Label

class HelloWorldApp(App):
    def build(self):
        # This returns the root widget of your application
        return Label(text='Hello, Kivy!')

if __name__ == '__main__':
    HelloWorldApp().run()
