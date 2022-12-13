import kivy
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
import time

GRID_SIZE = {"EASY": 3, "MEDIUM": 4, "HARD": 5, "IMPOSSIBLE": 25}
TIME_DISPLAYED = {"EASY": 3, "MEDIUM": 2, "HARD": 1, "IMPOSSIBLE": 0}
NUM_IMAGES = 9

playerCanAct = False
listOfCells = []
numImagesInCurrentSequence = 0
currentSequence = []
inputtedSequence = []



class Cell(BoxLayout):

    cellID = 1

    def __init__(self, pngType):
        super().__init__() 
        # * Gives each cell a unique id, self.cellID, which can be used to uniquely identify each cell object.
        self.cellID = Cell.cellID
        Cell.cellID += 1
        # * Chooses which button colour is used. This colour is selected randomely later on when the grid layout is made.
        pngLocation = "buttons/button{0}.png".format(pngType)
        self.imageDisplayed = Image(source = pngLocation)
        # * Adds a button to the cell, which will be displayed by default. Binds the handle_click function to each button.
        self.buttonDisplayed = Button()
        self.buttonDisplayed.bind(on_press = handle_click)
        self.add_widget(self.buttonDisplayed)
        # * Appends the cell to a list for access in main program.
        listOfCells.append(self)

    def display_image(self):
        # * Removes the button and adds the image.
        self.remove_widget(self.buttonDisplayed)
        self.add_widget(self.imageDisplayed)
        inputtedSequence.append(self)

    def hide_image(self):
        # * Removes the image and adds the button.
        self.remove_widget(self.imageDisplayed)
        self.add_widget(self.buttonDisplayed)
        inputtedSequence.remove(self)

    def auto_display_image(self):
        # * Remove the button and adds the image, called when displaying sequence to user.
        self.remove_widget(self.buttonDisplayed)
        self.add_widget(self.imageDisplayed)

    def auto_hide_image(self):
        # * Removes the image and adds the button, called when displaying sequence to user.
        self.remove_widget(self.imageDisplayed)
        self.add_widget(self.buttonDisplayed)



def handle_click(instance):
    instance.parent.display_image()

def iterate_sequence():
    # * Gets a random cell that is not in currentSequence and appends it to currentSequence.
    getButton = True
    while getButton == True:
        for button in range(len(listOfCells)):
            buttonToAppend = listOfCells[button]
            if buttonToAppend in currentSequence:
                pass
            else:
                currentSequence.append(buttonToAppend)
                getButton = False
                break

def display_sequence():
    # * Displays the sequence to the user.
    playerCanAct = False
    for button in currentSequence:
        button.auto_display_image()
        button.auto_hide_image()
    playerCanAct = True

def testing(delta):
    iterate_sequence()
    display_sequence()


class Application(App):

    def build(self):
        # * Adds the cells to the grid layout, assigning a random image each time.
        layout = GridLayout(cols = GRID_SIZE[difficulty])
        for row in range(GRID_SIZE[difficulty]):
            for col in range(GRID_SIZE[difficulty]):
                layout.add_widget(Cell(random.randrange(1, NUM_IMAGES + 1)))
        Clock.schedule_once(testing, TIME_DISPLAYED[difficulty])
        return (layout)

if __name__ == "__main__":
    difficulty = ((input("Enter difficulty (easy, medium or hard): ")).upper())
    myApp = Application()
    myApp.run()


# ! Continue the testing function to make sure everything's working :)