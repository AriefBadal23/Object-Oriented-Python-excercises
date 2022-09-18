# Shape class - basic

import random

# setup the colors
RED = (255,0,0)
GREEN = (0,255, 0)
BLUE = (0,0, 255)

class Shape():
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

    

