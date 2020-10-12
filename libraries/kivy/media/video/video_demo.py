from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.button import Button
from kivy.uix.image import Image
# start playing the video at creation


class VideoDemo(App):
    def build(self):
        video = Image(source='fb1.mp4')

        return Button(text="Hello world!", background_normal=(0, 0, 0, 0))


if __name__ == "__main__":
    VideoDemo().run()
