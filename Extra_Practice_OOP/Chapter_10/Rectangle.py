""" A rectangle class """

import random
import pygame
from Shape import Shape

class Rectangle(Shape):
    """ Class to create a Rectangle shape """
    def __init__(self, window, max_width, max_height):
        super().__init__(window, 'Rectangle', max_width, max_height)
        self.width = random.randrange(10,100)
        self.height = random.randrange(10,100)
        self.rect = pygame.Rect(self.x_position, self.y_position, self.width, self.height)

    def clicked_inside(self, mouse_point):
        """  Checks if the shape has been clicked inside """
        clicked = self.rect.collidepoint(mouse_point)
        return clicked

    def get_area(self):
        """ Returns the area of a clicked shape  """
        the_area = self.width * self.height
        return the_area

