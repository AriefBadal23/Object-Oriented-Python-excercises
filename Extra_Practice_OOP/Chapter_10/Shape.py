""" Shape class - basic which is used as base class for other classes """
from abc import ABC, abstractmethod
import random


# setup the colors
RED = (255,0,0)
GREEN = (0,255, 0)
BLUE = (0,0, 255)

class Shape(ABC):
    # Inherits from the ABC class, telling Python to prevent client code from
    # instantiating a Shape object directly. Any attempt to do so results in the folling error message
    # TypeError: Can't instatiate abstract class Shape with Abstract methods clicked_inside, draw, get_area
    
    """ Basic Shape class """
    def __init__(self, window, shape_type, max_width, max_height):
        self.window = window
        self.shape_type = shape_type
        self.color = random.choice((RED, GREEN, BLUE))
        self.x_position = random.randrange(1, max_width - 100)
        self.y_position = random.randrange(25, max_height - 100)

    def get_type(self):
        """ Returns the type of the shape object """
        return self.shape_type
    
    @abstractmethod
    def clicked_inside(self, mouse_point):
        """  Checks if the shape has been clicked inside """
        raise NotImplementedError

    def get_area(self):
        """ Returns the area of a clicked shape  """
        raise NotImplementedError
    
    def draw(self):
        """ Draws the shape on the surface  """
        raise NotImplementedError
    

