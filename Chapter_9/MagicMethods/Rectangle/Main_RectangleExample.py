import pygame
import sys
from pygame.locals import *
from Rectangle import *


# Setup the constants
WHITE = (255,255,255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_RECTANGLES = 10
FIRST_RECTANGLE = 'first'
SECOND_RECTANGLE = 'second'



#Set up the window 
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

rectangle_list = []
for item in range(0, N_RECTANGLES):
    oRectangle = Rectangle(window)
    rectangle_list.append(oRectangle)

which_rectangle = FIRST_RECTANGLE

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        if event.type == MOUSEBUTTONDOWN:
            for oRectangle in rectangle_list:
                if oRectangle.clicked_inside(event.pos):
                    print('Clicked on', which_rectangle, 'rectangle')

                if which_rectangle == FIRST_RECTANGLE:
                    ofirst_rectangle = oRectangle
                    which_rectangle = SECOND_RECTANGLE

                elif which_rectangle == SECOND_RECTANGLE:
                    osecond_rectangle = oRectangle
                    # User has chosen 2 rectangles lets compare
                    if ofirst_rectangle == osecond_rectangle:
                        print('Rectangles are the same size')

                    elif ofirst_rectangle < osecond_rectangle:
                        print('First rectangle is smaller than second rectangle')

                    else: #must be larger
                        print('First rectangle is larger than scond rectangle')
                    which_rectangle = FIRST_RECTANGLE

    # Clear the window and draw all rectangles
    window.fill(WHITE)
    for oRectangle in rectangle_list:
        oRectangle.draw()

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
