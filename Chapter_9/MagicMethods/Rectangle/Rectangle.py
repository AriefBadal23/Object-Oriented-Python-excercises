# Rectlangle class
import pygame
import random

# Setup the colors
RED = (255,000)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Rectangle():
    def __init__(self, window):
        self.window = random.choice((20, 30, 40))
        self.width = random.choice((20, 30, 40))
        self.height = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(0, 400)
        self.y = random.randrange(0, 400)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.area = self.width * self.height

        def clicked_inside(self, mouse_point):
            clicked = self.rect.collidepoint(mouse_point)
            return clicked

        # Magic methods called when you compare
        # Two rectangle objects with the == operator

        def __eq__(self, oOther_rectangle, rectangle):
            if self.area == oOther_rectangle.area:
                return True
            else:
                return False

        
        # Magic method called when you compare two rectangle objects with the
        # < operator

        def __lt__(self, oOther_rectangle):
            if not isinstance(oOther_rectangle, Rectangle):
                raise TypeError("Second object was not an a Rectangle")
            if self.area < oOther_rectangle:
                return True

            else: 
                return False


        # Magic method called when you compare two rect. objects with the > operator
        def __gt__(self, oOther_rectangle):
            if not isinstance(oOther_rectangle, Rectangle):
                raise TypeError('Second object was not a Rectangle')

            if self.area > oOther_rectangle.area:
                return True
            
            else:
                return False



        def get_area(self):
            return self.area

        
        def draw(self):
            pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))




# Magic methods
# client code
# __lt__() == larger then