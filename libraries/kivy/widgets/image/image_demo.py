from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout

class ImageDemo(App):
    def build(self):
        layout = GridLayout(cols=2)
        image = Image(source="../../resources/Rect_icon.png")
        layout.add_widget(image)
        return layout


if __name__ == "__main__":
    ImageDemo().run()