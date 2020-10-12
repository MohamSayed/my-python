from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


# Custom [GridLayout]
class CustomGridLayout(GridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        self.add_widget(Button(text="Custom grid button"))


class GridLayoutDemo(App):
    def build(self):
        layout = CustomGridLayout(cols=2)

        button = Button(text='Button 1')
        button.color = (1, 0.5, 0.5, 1)

        # callback
        button.bind(on_press=self.callback)
        button2 = Button(text='Button 2')

        # adding to gridlayout
        layout.add_widget(button)
        layout.add_widget(button2)
 

        return layout

    def callback(instance, value):
        print('Button pressed')


GridLayoutDemo().run()
