import kivy
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image




class Cell(BoxLayout):
    def __init__(self, image_id):
        super().__init__()
        image_location = 'assets/image{0}.png'.format(image_id)
        self.imageView = Image(source=image_location)
        self.buttonView = Button()
        self.buttonView.bind(on_press=self.reveal_image)
        self.add_widget(self.buttonView)

    def reveal_image(self, instance):
        self.remove_widget(self.buttonView)
        self.add_widget(self.imageView)
        Clock.schedule_once(self.hide_image, 2)

    def hide_image(self, instance):
        self.remove_widget(self.imageView)
        self.add_widget(self.buttonView)

class Application(App):
    def build(self):
        layout = GridLayout(cols=4)
        for row in range(4):
            for col in range(4):
                layout.add_widget(Cell(random.randint(1, 6)))
        return layout


if __name__ == "__main__":
    myApp = Application()
    myApp.run()