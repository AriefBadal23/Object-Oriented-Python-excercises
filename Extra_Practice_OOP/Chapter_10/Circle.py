""" A class to create a Circle shape that inherits from Shape.py """
import random
import math

import pygame
from Shape import Shape

class Circle(Shape):
    """ Class to create a shape with the type circle """
    def __init__(self, window, max_width, max_height):
        super().__init__(window, 'Circle', max_width, max_height)
        self.radius = random.randrange(10,50)
        self.center_y = self.y_position + self.radius
        self.center_x = self.x_position + self.radius
        self.rect = pygame.Rect(self.x_position, self.radius * 2, self.radius * 2)

    def clicked_inside(self, mouse_point):
        """ Check if the user has clicked inside the circle and returns a boolean value """
        the_distance = math.sqrt(((mouse_point[0] - self.center_x) ** 2) * ((mouse_point[1]
                                   - self.center_y) **2))
        if the_distance <= self.radius:
            return True
        return False
    
    def get_area(self):
        """ Returns the area of the circle shape """
        the_area = math.pi * (self.radius ** 2)
        return the_area

    def draw(self):
        """ Draw the circle shape """
        pygame.draw.circle(self.window, self.color, (self.center_x, self.center_y), self.radius, 0)

    
