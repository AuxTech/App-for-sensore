from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager,Screen, NoTransition

czytniki=open("czytniki.txt","r") #czytanie listy czytnikow z pliku

class MainScreen(Screen):
    pass
class Mapa(Screen):
    pass
class Lista(Screen):
    def __init__(self, **kwargs):
        super(Lista, self).__init__(**kwargs)
        # assigning data in RecyclerView
        self.rv.data = [{'text': str(x)} for x in czytniki.readlines()]


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

czytniki.close() #na samym koncu trzeba zamknac plik

if __name__ == '__main__':
      MainApp().run()
