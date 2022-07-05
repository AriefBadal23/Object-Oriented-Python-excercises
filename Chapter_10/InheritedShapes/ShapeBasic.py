import random
import pygame

# Set up the colors
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)

""" Base class to create other shapes """
class Shape():
    def __init__(self, window, shapeType, max_width, max_height):
        """ Remembers the data passed in in instance variables,
        then randomly choose a color and a starting location (self.x and self.y)"""
        self.window = window
        self.shapeType = shapeType
        self.color = random.choice(RED, GREEN, BLUE)
        self.x = random.randrange(1, max_width - 100)
        self.y = random.randrange(25, max_height - 100)
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
    
    def get_type(self):
        """ Returns the type of shape of given at initialization """
        return self.shape_type



