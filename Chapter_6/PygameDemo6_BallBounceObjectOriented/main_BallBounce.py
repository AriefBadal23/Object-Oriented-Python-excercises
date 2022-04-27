# pygame demo 4(a) - one image, move by keyboard
""" Small programs that allows to move the ball image using the keyboard """

# Import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *  # bring in the Ball class code

# Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 400
FRAMERS_PER_SECOND = 30


# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 5 Initialize the variables
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)


# Loop forever
while True:
    # Check for and handle events:
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the balls location, using the speed in two directions
    oBall.update()  # tell the Ball to update itself 

    # Clear the window before drawing it again
    window.fill(BLACK)

    # 10 Draw the window elements
    oBall.draw()  # tell the Ball to draw itself

    # Update the window
    pygame.display.update()

    # Slow thing down a bit
    clock.tick(FRAMERS_PER_SECOND)
