import kivy
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

GRID_SIZE = 4
IMAGE_COUNT = 6
MAX_IMAGES_VISIBLE = 3

# Stored the list of all Cell objects with images currently revealed.
selected_cells = []


def handle_click(instance):
    """This function is called when a button is clicked."""
    if len(selected_cells) < MAX_IMAGES_VISIBLE:
        # instance is the Button clicked, not the Cell. 
        # We need to call reveal_image() on Cell object instead,
        # which is the parent view of that Button.
        instance.parent.reveal_image()  

class Cell(BoxLayout):
    """Each cell contains a button and an image.
    Only one of these two are visible at any given time.
    When the button is clicked, it is replaced by the image for 4s.
    """

    def __init__(self, image_id):
        super().__init__() 
        # image_id might be useful to compare if two images are the same
        self.imageId = image_id
        image_location = 'assets/image{0}.png'.format(image_id)
        self.imageView = Image(source=image_location)

        self.buttonView = Button()
        self.buttonView.bind(on_press=handle_click)
        # At the start, the cell shows the button (not the image)
        self.add_widget(self.buttonView)


    def reveal_image(self):
        """Removes button view and presents image view in the cell."""
        self.remove_widget(self.buttonView)
        self.add_widget(self.imageView)
        selected_cells.append(self)
        # This will schedule a call to self.hide_image() after 4 seconds.
        Clock.schedule_once(self.hide_image, 4)

    # Note that callbacks scheduled using Clock need a *delta* argument, which
    # indicates time in seconds (as a float) since the event was scheduled.
    def hide_image(self, delta):
        """Removes image view and presents button view in the cell."""
        self.remove_widget(self.imageView)
        self.add_widget(self.buttonView)
        selected_cells.remove(self)


class Application(App):

    def build(self):
        """Creates a GRID_SIZExGRID_SIZE matrix of Cell objects with
        underlying images assigned randomly.
        """
        layout = GridLayout(cols=GRID_SIZE)
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                layout.add_widget(Cell(random.randint(1, IMAGE_COUNT)))
        return layout

if __name__ == "__main__":
    myApp = Application()
    myApp.run()