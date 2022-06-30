import random
import pygame

# Set up the colors
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)

class Shape():
    """ Base class to create other shapes """
    def __init__(self, window, color, max_width, max_height):
        self.window = window
        self.color = color
        self.x = random.randrange(1, max_width - 100)
        self.y = random.randrange(25, max_height - 100)
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
    
    def get_type(self):
        return self.shape_type



        