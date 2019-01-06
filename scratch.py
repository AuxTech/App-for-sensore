from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen, FadeTransition

class MainScreen(Screen):
    pass
class Mapa(Screen):
    pass
class Lista(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


presentation= Builder.load_file("SimpleKivy.kv")
class MainApp(App):

    def build(self):
        return presentation
if __name__ == '__main__':
      MainApp().run()
