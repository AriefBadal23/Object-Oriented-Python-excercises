from Shape import *
import random
import pygame

class Triangle(Shape):

    def __init__(self, window, max_width, max_height):
        super().__init__(window, 'Triangle', max_width, max_height)
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.triange_slope = -1 * (self.height / self.width)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def clicked_inside(self, mouse_point):
        inRect = self.rect.collidepoint(mouse_point)
        if not inRect:
            return False
        # Do some math to see if the point is inside the triangle
        x_Off_set = mouse_point[0] - self.y
        y_Off_set = mouse_point[1] - self.y
        if x_Off_set == 0:
            return True

        point_slope_from_intercept = (y_Off_set - self.height) / x_Off_set #rise over run
        if point_slope_from_intercept < self.triange_slope:
            return True
        else:
            return False
        
    def get_area(self):
        the_area = .5 * self.width * self.height
        return the_area

    def draw(self):
        pygame.draw.polygon(self.window, self.color, (
            (self.x, self.y + self.height),
            (self.x, self.y),
            (self.x + self.width, self.y)))


# BUG OPLOSSEN