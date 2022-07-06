# Shape class
#
# To be used as a base class for other classes

import random
from abc import ABC, abstractmethod

# Set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Shape(ABC): # Identifies this as an abstract base class
    def __init__(self, window, shapeType, max_width, max_height):
        """ Remembers the data passed in in instance variables,
        then randomly choose a color and a starting location (self.x and self.y)"""
        self.window = window
        self.shape_type = shapeType
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(1, max_width - 100)
        self.y = random.randrange(25, max_height - 100)
    
    def get_type(self):
        """ Returns the type of shape of given at initialization """
        return self.shape_type

    @abstractmethod
    def clicked_inside(self, mouse_point):
        raise NotImplementedError

    @abstractmethod
    def get_area(self):
        raise NotImplementedError

    @abstractmethod
    def draw(self):
        raise NotImplementedError