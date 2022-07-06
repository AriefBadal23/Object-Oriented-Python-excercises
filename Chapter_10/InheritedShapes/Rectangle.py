from turtle import color
import pygame
from Shape import *

class Rectangle(Shape):
    def __init__(self, window, max_width, max_height):
        super().__init__(window, 'Rectangle', max_width, max_height)
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def clicked_inside(self, mouse_point):
        clicked = self.rect.collidepoint(mouse_point)
        return clicked

    def get_area(self):
        the_area= self.width * self.height
        return the_area

    def draw(self):
      pygame.draw.rect(self.window, BLUE, (self.x, self.y, self.width, self.height))