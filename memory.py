import kivy
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

selected_cells = []

def handle_click(instance):
    print(len(selected_cells))
    if len(selected_cells) < 3:
        instance.parentCell.reveal_image()  

class Cell(BoxLayout):
    def __init__(self, image_id):
        super().__init__()
        self.imageId = image_id
        self.isDisabled = False
        image_location = 'assets/image{0}.png'.format(image_id)
        self.imageView = Image(source=image_location)
        self.buttonView = Button()
        self.buttonView.bind(on_press=handle_click)
        self.buttonView.parentCell = self
        self.add_widget(self.buttonView)

    def reveal_image(self):
        self.remove_widget(self.buttonView)
        self.add_widget(self.imageView)
        self.isDisabled = True
        selected_cells.append(self)
        Clock.schedule_once(self.hide_image, 5)

    def hide_image(self, instance):
        self.remove_widget(self.imageView)
        self.add_widget(self.buttonView)
        selected_cells.remove(self)
        self.isDisabled = False


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