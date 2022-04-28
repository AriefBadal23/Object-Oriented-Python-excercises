from turtle import window_height, window_width
import pygame

from pygame.locals import *
import random

# Ball class
class Ball():
    def __init__(self, window, window_width, window_height):
        self.window = window # remember the window, so we can draw later
        self.window_width = window_width
        self.window_height = window_height

        self.image = pygame.image.load('images/ball.png')
        # A rect is made up of [x, y, width, height]
        ball_rect = self.image.get_rect()
        self.width = ball_rect.width
        self.height = ball_rect.height
        self.max_width = window_width - self.width
        self.max_height = window_height - self.height


        # Pick a random starting position
        self.x = random.randrange(0, self.max_width)
        self.y = random.randrange(0, self.max_height)

        # Choose a random speed between -4 and 4, but not zero,
        # in both the x and y directions
        speeds_list = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speeds_list)
        self.ySpeed = random.choice(speeds_list)


    def update(self):
        # Check for hitting a wall. if so, change that direction
        if (self.x < 0) or (self.x >= self.max_width):
            self.xSpeed= - self.xSpeed


        if (self.y < 0) or (self.y >= self.max_height):
            self.ySpeed =- self.ySpeed

        # Update the Ball's x and y, using the speed in two directions
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image,(self.x, self.y))

