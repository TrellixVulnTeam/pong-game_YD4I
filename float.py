import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class XApp(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    XApp().run()
