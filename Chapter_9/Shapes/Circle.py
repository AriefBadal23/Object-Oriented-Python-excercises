#  Circle class

import pygame
import random
import math

# Set up the colors
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)

class Circle():
    def __init__(self, window, max_width, max_height):
        self.window = window

        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(1, max_width - 100)
        self.y = random.randrange(25, max_height - 100)
        self.radius = random.randrange(10, 50)
        self.center_x = self.x + self.radius
        self.center_y = self.y + self.radius
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.shape_type = 'Circle'


    
    def clicked_inside(self, mouse_point):
        distance = math.sqrt(((mouse_point[0] - self.center_x) ** 2) +
        ((mouse_point[1] - self.center_y) **2))

        if distance <= self.radius:
            return True
        else:
            return False
    
    def get_area(self):
        the_area = math.pi * (self.radius ** 2)
        return the_area

    def get_type(self):
        return self.shape_type

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.center_x, self.center_y), self.radius, 0)

    