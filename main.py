from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import webbrowser
import time
from filesharer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        """Starts the webcam"""
        self.ids.camera.play = True
        self.ids.start_stop.text = "Stop Camera"

    def stop(self):
        """Stops the webcam"""
        self.ids.camera.play = False
        self.ids.start_stop.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        """
        Captures a picture from the webcam and saves it to filepath with
        the name of the current time
        """
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = "pictures/" + current_time + ".png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    link_message: "Create Link First"

    def create_link(self):
        """Accesses the photo filepath, uploads it to the web, and inserts the
        link in the Label widget"""
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        fileshare = FileSharer(filepath=file_path)
        self.url = fileshare.share()
        self.ids.link_text.text = str(self.url)

    def copy_link(self):
        """Copies the link in the Label widget to the clipboard"""
        try:
            Clipboard.copy(str(self.url))
        except:
            self.ids.link_text.text = self.link_message

    def open_link(self):
        """Opens the link from the Label widget on the web"""
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link_text.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
