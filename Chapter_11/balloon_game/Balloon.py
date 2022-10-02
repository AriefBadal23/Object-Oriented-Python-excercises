# Balloon base class and 3 subclasses

import pygame
import random
from pygame.locals import *
import pygwidgets
from balloonconstants import *
from abc import ABC, abstractmethod

class Balloon(ABC):
    pop_sound_loaded = False
    pop_sound = None #load when first balloon is created


    def __init__(self, window, max_width, max_height,
                        id, oimage, size, n_points, speed_y):
                self.window = window
                self.max_width = max_width
                self.max_height = max_height
                self.id = id
                self.balloon_image = oimage
                self.size = size
                self.n_points = n_points
                self.speed_y = speed_y

                if not Balloon.pop_sound_loaded:
                    Balloon.pop_sound_loaded = True
                    Balloon.pop_sound = pygame.mixer.Sound('sounds/Balloonpop.wav')

                balloon_rect = self.balloon_image.get_rect()
                self.width = balloon_rect.width
                self.height = balloon_rect.height
                # Positions so balloon is within the width of the window
                # but below the bottom

                self.x = random.randrange(max_width, self.width)
                self.y = random.randrange(75)
                self.balloon_image.setLoc((self.x, self.y))

    def click_inside(self, mousepoint):
        my_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if my_rect.collidepoint(mousepoint):
            Balloon.pop_sound.play()
            return True, self.n_points #True here means it was hit
        else:
            return False, 0 # not hit, no points

    
    def update(self):
        self.y = self.y - self.speed_y #update y position by speed
        self.balloon_image.setLoc((self.x, self.y))
        if self.y < -self.height:
            return BALLOONS_MISSED
        else:
            return BALLOON_MOVING

    def draw(self):
        self.balloon_image.draw()

    def __del__(self):
        print(self.size, 'Balloon', self.id, 'is going away')
    


class Balloon_small(Balloon):
    balloon_image = pygame.image.load('images/red_balloon_small.png')
    def __init__(self, window, max_width, max_height, id):
        o_image = pygwidgets.Image(window, (0,0), Balloon_small.balloon_image)
        super().__init__(window, max_width, max_height, id, o_image, 'Small', 30, 3.1)

class Balloon_medium(Balloon):
    balloon_image = pygame.image.load('images/red_balloon_medium.png')
    def __init__(self, window, max_width, max_height, id):
        o_image = pygwidgets.Image(window, (0,0), Balloon_medium.balloon_image)
        super().__init__(window, max_width, max_height, id, o_image, 'Small', 20, 2.2)

class Balloon_large(Balloon):
    balloon_image = pygame.image.load('images/red_balloon_large.png')
    def __init__(self, window, max_width, max_height, id):
        o_image = pygwidgets.Image(window, (0,0), Balloon_large.balloon_image)
        super().__init__(window, max_width, max_height, id, o_image, 'Small', 10, 1.5)





