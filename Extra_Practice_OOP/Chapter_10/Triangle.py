""" A class to create a Triangle shape that inherits from Shape.py """

import random
import pygame
from Shape import Shape

class Triangle(Shape):
    """ Triangle class to create a Triangle shape """
    def __init__(self, window, max_width, max_height):
        super().__init__(window, 'Triangle', max_width, max_height)
        self.width = random.randrange(10,100)
        self.height = random.randrange(10,100)
        self.triangle_slope = -1 * (self.height / self.width)
        self.rect = pygame.Rect(self.x_position, self.y_position, self.width, self.height)

    def clicked_inside(self, mouse_point):
        """ Check if the user has clicked inside the circle and returns a boolean value """
        in_rect = self.rect.collidepoint(mouse_point)
        if not in_rect:
            return False

        # Do some math to see if the point is inside the triangle
        x_offset = mouse_point[0] - self.x_position
        y_offset = mouse_point[1] - self.y_position
           
        if x_offset == 0:
            return True

        point_slope_from_intercept = (y_offset - self.height / x_offset) # Never rise over run
        if point_slope_from_intercept < 1:
            return True
        return False

    def get_area(self):
        """ Returns the area of the triangle shape """
        the_area = 5 * self.width * self.height
        return the_area

    def draw(self):
        """ Method to draw a triangle shape of the surface """
        pygame.draw.polygon(self.window, self.color, (self.x_position + self.height),
                                                    (self.x_position, self.y_position),
                                                    (self.x_position + self.width, self.y_position))
