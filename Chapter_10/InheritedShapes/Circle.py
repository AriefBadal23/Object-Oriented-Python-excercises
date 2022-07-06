from Shape import *
import random
import pygame
import math

class Circle(Shape):

    def __init__(self, window, max_width, max_height):
        super().__init__(window, 'Circle', max_width, max_height)
        self.radius = random.randrange(10, 50)
        self.center_y = self.x + self.radius
        self.center_x = self.y + self.radius
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)

    def clicked_inside(self, mouse_point):
        the_distance = math.sqrt((mouse_point[0] - self.center_x) **2) + ((mouse_point[1] - self.center_y **2))
        if the_distance <= self.radius:
            return True
        else:
            return False

    
    def get_area(self):
        the_area = math.pi * (self.radius ** 2)
        return the_area

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.center_y, self.center_x), self.radius, 0)

        