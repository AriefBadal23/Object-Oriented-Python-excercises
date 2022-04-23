# Pygame demo 0 - window only

# Template to create a pygame window


# Import packages
import pygame
from pygame.locals import *
import sys


BLACK = (0,0,0)
WINDOWN_WIDTH = 640
WINDOWN_HEIGHT = 400
FRAMERS_PER_SECOND = 30


# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOWN_WIDTH, WINDOWN_HEIGHT))
clock = pygame.time.Clock()



# Load the assets: image(s), sound(s), etc.
ball_image = pygame.image.load('images/ball.png')

# Initialize the variables

# Loop forever
while True:
    # Check for and handle events:
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Do any "per frame" actions

    # Clear the window
    window.fill(BLACK)

    # Draw all window elements
    # draw ball at position 100 accross(x) and 200 down (y)
    window.blit(ball_image, (100, 200))

    # Update the window
    pygame.display.update()


    # Slow thing down a bit
    clock.tick(FRAMERS_PER_SECOND) # make pygame wait 

    