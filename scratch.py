from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen, NoTransition



class MainScreen(Screen):
    pass
class Mapa(Screen):
    pass
class Lista(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

Builder.load_file("SimpleKivy.kv")

sm = ScreenManager(transition=NoTransition())
sm.add_widget(MainScreen(name='main'))
sm.add_widget(Mapa(name='mapa'))
sm.add_widget(Lista(name='lista'))

class MainApp(App):

    def build(self):
        return sm
if __name__ == '__main__':
      MainApp().run()
