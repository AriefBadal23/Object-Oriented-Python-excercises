# pygame demo 4(b) - one image, bounce around the window using rects with sound
# Note: this excercise has a little bug; I get the following error message: pygame.error: Failed loading libmpg123-0.dll:
# Import packages

import pygame
from pygame.locals import *
import sys
import random
from pygame import mixer


BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 400
FRAMERS_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3


# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load the assets: image(s), sound(s), etc.
mixer.init()
ball_Image = pygame.image.load('images/ball.png')
bounce_sound = pygame.mixer.Sound('sounds/boing.wav')
mixer.music.load('sounds/background.mp3')
mixer.music.play(-1, 0.0)



# Initialize the variables
ball_rect = ball_Image.get_rect()
MAX_WIDTH = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
ball_rect.left = random.randrange(MAX_WIDTH)
ball_rect.top = random.randrange(MAX_HEIGHT)
x_Speed = N_PIXELS_PER_FRAME
y_Speed = N_PIXELS_PER_FRAME

# Loop forever
while True:
    # Check for and handle events:
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        # Do any "per frame" actions
        if (ball_rect.left < 0) or (ball_rect.right >= MAX_WIDTH):
            x_Speed = -x_Speed # reverse X direction
            bounce_sound.play()

        if (ball_rect.top < 0) or (ball_rect.bottom >= MAX_HEIGHT):
            y_Speed = -y_Speed # reverse Y direction
            bounce_sound.play()

        # Update the balls rectangle, using the speed in two directions
        ball_rect.left = ball_rect.left + x_Speed
        ball_rect.top = ball_rect.top + y_Speed
        

    # Clear the window before drawing it again
    window.fill(BLACK)

    # Draw the window elements
    window.blit(ball_Image, ball_rect)

   
    # Update the window
    pygame.display.update()


    # Slow thing down a bit
    clock.tick(FRAMERS_PER_SECOND)


    