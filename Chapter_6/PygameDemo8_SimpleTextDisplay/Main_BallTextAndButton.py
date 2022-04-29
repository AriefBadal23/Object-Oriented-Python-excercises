# pygame demo 4(a) - one image, move by keyboard
""" Small programs that allows to move the ball image using the keyboard """

# Import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *  # bring in the Ball class code
from SimpleText import *
from SimpleButton import *

# Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 400
FRAMERS_PER_SECOND = 30


# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 5 Initialize the variables
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oFrameCountLabel = SimpleText(
    window, (60, 20), "Programming has run through this many loops", WHITE
)
oFrameCountDisplay = SimpleText(window, (500, 20), "", WHITE)
ORestartButton = SimpleButton(
    window, (200, 60), "images/restartUp.png", "images/restartDown.png"
)
frameCounter = 0

# Loop forever
while True:
    # Check for and handle events:
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ORestartButton.handleEvent(event):
            frameCounter = 0  # clicked button, reset counter

    # Do any 'per frame' actions
    oBall.update()  # tell the Ball to update itself
    frameCounter = frameCounter + 1  # increment each frame
    oFrameCountDisplay.setValue(str(frameCounter))

    # Clear the window before drawing it again
    window.fill(BLACK)

    # 10 Draw the window elements
    oBall.draw()  # tell the Ball to draw itself
    oFrameCountDisplay.draw()
    ORestartButton.draw()

    # Update the window
    pygame.display.update()

    # Slow thing down a bit
    clock.tick(FRAMERS_PER_SECOND)
