import pygame
import sys
from pygame.locals import *
from Square import *
from Circle import *
from Triangle import *
from Rectangle import *
import pygwidgets


# set up the constants
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_SHAPES = 10


# Set up the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

shapes_list = []
shape_classes_tuple= (Square, Circle, Triangle, Rectangle)

for shape in range (0, N_SHAPES):
    randomlyChosenClass = random.choice(shape_classes_tuple)
    oShape = randomlyChosenClass(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    shapes_list.append(oShape)

oStatusLine = pygwidgets.DisplayText(window, (4,4), 'Click on shapes', fontSize=28)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            # Reverse order to check last drawn shape first
            for oShape in reversed(shapes_list):
                if oShape.clicked_inside(event.pos):
                    area = oShape.get_area()
                    area = str(area)
                    theType = oShape.get_type()
                    newText = 'Clicked on a ' + theType + 'whose area is ' + area
                    oStatusLine.setValue(newText)
                    break # only deal with topmost shape

    # Tell each shape to draw itself
    window.fill(WHITE)
    for Oshape in shapes_list:
        Oshape.draw()
    oStatusLine.draw()

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)