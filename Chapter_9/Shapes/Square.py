# Square class
import pygame
import random



# Set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Square():
    def __init__(self, window, max_width, max_height):
        self. window = window
        self.width_and_height = random.randrange(10, 100)
        self.color = random.choice(RED, GREEN, BLUE)
        self.x = random.randrange(1, max_width - 100)
        self.y = random. randrange(25, max_height -100)
        self.rect = pygame.Rect(self.x, self.y, self.width_and_height, self.width_and_height)
        self.shapetype = 'Square'

    def clicked_inside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked

    def get_type(self):
        return self.shapetype

    def get_area(self):
        the_area = self.width_and_height * self.width_and_height
        return the_area

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.x, self.y, self.width_and_height, self.width_and_height)
