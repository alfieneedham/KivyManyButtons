import kivy
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

GRID_SIZE = {"EASY": 5, "MEDIUM": 7, "HARD": 9, "IMPOSSIBLE": 25}
TIME_DISPLAYED = {"EASY": 5. "MEDIUM": 4, "HARD": 3, "IMPOSSIBLE": 0}
NUM_IMAGES = 9

numImagesInCurrentSequence = 0
currentSequence = []
inputtedSequence = []

difficulty = input("Enter difficulty [easy, medium or hard): ")



class Cell(BoxLayout):

    cellID = 1

    def __init__(self, pngType):
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

    def display_image(self):
        # * Removes the button and adds the image. Schedules the hide_image function to activate after the set time.
        self.remove_widget(self.buttonDisplayed)
        self.add_widget(self.imageDisplayed)
        inputtedSequence.append(self)
        Clock.schedule_once(self.hide_image, TIME_DISPLAYED[difficulty])

    def hide_image(self, delta):
        # * Removes the image and adds the button. This happens after a set time.
        self.remove_widget(self.imageDisplayed)
        self.add_widget(self.buttonDisplayed)
        inputtedSequence.remove(self)