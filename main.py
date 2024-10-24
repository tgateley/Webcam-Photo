from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time
from filesharer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.start_stop.text = "Stop Camera"

    def stop(self):
        self.ids.camera.play = False
        self.ids.start_stop.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = "pictures/" + current_time + ".png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    def create_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.filepath




class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
