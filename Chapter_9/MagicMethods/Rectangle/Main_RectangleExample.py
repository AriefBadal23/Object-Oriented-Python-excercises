from shutil import which
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

pygame.init()
window  = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()


rectangle_list = []
for i in range(0, N_RECTANGLES):
    ORectangle = Rectangle(window)
    rectangle_list.append(ORectangle)

which_rectangle = FIRST_RECTANGLE



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if ORectangle in rectangle_list:
                if ORectangle in rectangle_list:
                    if ORectangle.clicked_inside(event.pos):
                        print('Clicked on', which_rectangle, 'rectangle')

                        if which_rectangle == FIRST_RECTANGLE:
                            oFirstRectangle = ORectangle
                            which_rectangle = SECOND_RECTANGLE

                        elif which_rectangle == SECOND_RECTANGLE:
                            oSecondRectangle = ORectangle
                            oSecondRectangle < ORectangle
                            print('First rectangle is smaller than second rectangle.')
                        else:
                             print('First rectangle is larger than second rectangle.')
                        whichRectangle = FIRST_RECTANGLE

    # Clear the window an draw all rectangless
    window.fill(WHITE)
    for oRectangle in rectangle_list:
        ORectangle.draw()

    pygame.display.update
    clock.tick(FRAMES_PER_SECOND)