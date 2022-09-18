""" A class to create a Square shape that inherits from Shape.py """
import random
import pygame
from Shape import Shape


class Square(Shape):
    """ Create a shape with the type Square """
    def __init__(self, window, max_width, max_height):
        super().__init__(window, 'Square', max_width, max_height)
        self.width_and_height = random.randrange(10,100)
        self.rect = pygame.Rect(self.x_position, self.y_position,
                                self.width_and_height, self.width_and_height)


    def clicked_inside(self, mouse_point):
        """  Checks if the shape has been clicked inside """
        clicked = self.rect.collidpoint(mouse_point)
        return clicked

    def get_area(self):
        """ Returns the area of a clicked shape  """
        the_area = self.width_and_height * self.width_and_height
        return the_area

    def draw(self):
        """ Draws the shape on the surface  """
        pygame.draw.rect(self.window, self.color, (self.x_position, self.y_position,
                                                   self.width_and_height, self.width_and_height))
