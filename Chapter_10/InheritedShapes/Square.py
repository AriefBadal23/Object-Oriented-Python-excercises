from Shape import *
import random
import pygame

class Square(Shape):
    def __init__(self, window, max_width, max_height):
        super().__init__(window, 'Square', max_width, max_height)
        self.width_and_height = random.randrange(10, 100)
        self.rect = pygame.Rect(self.x, self.y, self.width_and_height,self.width_and_height)

    def clicked_inside(self, mouse_point):
        clicked = self.rect.collidepoint(mouse_point)
        return clicked

    def get_area(self):
        the_area= self.width_and_height * self.width_and_height
        return the_area

    def draw(self):
        pygame.draw.rect(self.window, self.color,
                        (self.x, self.y, 
                        self.width_and_height, self.width_and_height))


        
        

