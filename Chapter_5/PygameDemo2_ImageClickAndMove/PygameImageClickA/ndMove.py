# Pygame demo 0 - window only

# Template to create a pygame window


# Import packages
import pygame
from pygame.locals import *
import sys
import random

BLACK = (0, 0, 0)
WINDOWN_WIDTH = 640
WINDOWN_HEIGHT = 400
FRAMERS_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOWN_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOWN_HEIGHT - BALL_WIDTH_HEIGHT


# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOWN_WIDTH, WINDOWN_HEIGHT))
clock = pygame.time.Clock()


# Load the assets: image(s), sound(s), etc.
ball_image = pygame.image.load("images/ball.png")


# Initialize the variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ball_rect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

# Loop forever
while True:
    # Check for and handle events:
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # see if the user clicked
        if event.type == pygame.MOUSEBUTTONUP:
            # mouseX, mouseY = event.pos   #  Could do this if we needed it

            # Check if the click was in the rect of the ball
            # If so, choose a random new location
            if ball_rect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ball_rect = pygame.Rect(
                    ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT
                )

    # Do any "per frame" actions

    # Clear the window
    window.fill(BLACK)

    # Draw all window elements
    # Draw the ball at the randomized location
    window.blit(ball_image, (ballX, ballY))

    # Update the window
    pygame.display.update()

    # Slow thing down a bit
    clock.tick(FRAMERS_PER_SECOND)  # make pygame wait
