import pygame
import random

# Setup the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Triangle():
    def __init__(self, window, max_width, max_height):
        self.window = window
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.triangle_scope = -1 * (self.height / self.width)

        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(1, max_width - 100)
        self.y = random.randrange(25, max_height - 100)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.shape_type = 'Triangle'


    def clicked_inside(self, mouse_point):
        in_rect = self.rect.collidepoint(mouse_point)
        if not in_rect:
            return False

        # Do some math to see if the point is inside the triangle
        x_offset = mouse_point[0] - self.x
        y_offset = mouse_point[1] - self.y
        
        if x_offset == 0:
            return True

        
        # Calculate the slope (rise over run)
        point_slope_from_y_intercept = (y_offset - self.height) / x_offset
        if point_slope_from_y_intercept < self.triangle_scope:
            return True
        else:
            return False

    
    def get_type(self):
        return self.shape_type


    def get_area(self):
        the_area = 5 * self.width * self.height
        return the_area

    
    def draw(self):
        pygame.draw.polygon(self.window, self.color,
                            ((self.x, self.y + self.height),
                            (self.x, self.y),
                            (self.x + self.width, self.y)))
