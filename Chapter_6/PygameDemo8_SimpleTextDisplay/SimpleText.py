import pygame
from pygame.locals import *

class SimpleText():
    def __init__(self, window, loc, value, textColor):
        # Instance variables with the inital values of the class objects
        pygame.font.init()
        self.window = window
        self.loc = loc
        self.font = pygame.font.SysFont(None, 30)
        self.text_color = textColor
        self.text = None # so that the call to setText below will force the creation of the text image
        # Calling the setValue method to create the new text
        self.setValue(value) # set the initial text for drawing


    def setValue(self, new_text):
        """ Method to set the initial value for the text image """

        # Checks if the last text rendered is the same as the new text
        if self.text == new_text:
         return # nothing to change

        self.text = new_text
        self.text_surface = self.font.render(self.text, True, self.text_color)


    def draw(self):
        """ Method to draw the text image on the screen """
        self.window.blit(self.text_surface, self.loc)



