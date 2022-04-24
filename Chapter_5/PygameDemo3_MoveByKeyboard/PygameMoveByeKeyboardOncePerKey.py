# pygame demo 3(a) - one image, move by keyboard
""" Small programs that allows to move the ball image using the keyboard """

# Import packages
import pygame
from pygame.locals import *
import sys
import random


BLACK = (0,0,0)
WINDOWN_WIDTH = 640
WINDOWN_HEIGHT = 400
FRAMERS_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOWN_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOWN_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3


# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOWN_WIDTH, WINDOWN_HEIGHT))
clock = pygame.time.Clock()



# Load the assets: image(s), sound(s), etc.
ball_Image = pygame.image.load('images/ball.png')
target_Image = pygame.image.load('images/target.jpg')



# Initialize the variables
ball_X = random.randrange(MAX_WIDTH)
ball_Y = random.randrange (MAX_HEIGHT)
target_Rect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)


# Loop forever
while True:
    # Check for and handle events:
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # See if the user pressed a key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_X = ball_X - N_PIXELS_TO_MOVE

            elif event.key == pygame.K_RIGHT:
                ball_X = ball_X  + N_PIXELS_TO_MOVE

            elif event.key == pygame.K_UP:
                ball_Y = ball_Y - N_PIXELS_TO_MOVE

            elif event.key == pygame.K_DOWN:
                ball_Y = ball_Y + N_PIXELS_TO_MOVE
    # Do any "per frame" actions
    # Check if the ball is colliding with the target
    ball_Rect = pygame.Rect(ball_X, ball_Y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    # Checks if two rectangeles overlap (ball rectangle and target rectangle)
    if ball_Rect.colliderect(target_Rect):
        print('Ball is touching the target')
    
    
    # Clear the window
    window.fill(BLACK)

    # Draw all window elements
    window.blit(target_Image, (TARGET_X, TARGET_Y)) # draw the target
    window.blit(ball_Image, (ball_X, ball_Y)) # draw the ball

   
    # Update the window
    pygame.display.update()


    # Slow thing down a bit
    clock.tick(FRAMERS_PER_SECOND)


    