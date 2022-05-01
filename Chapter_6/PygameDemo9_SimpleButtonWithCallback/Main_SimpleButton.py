# pygame demo 4(a) - one image, move by keyboard
""" Small programs that allows to move the ball image using the keyboard """

# Import packages
import pygame
from pygame.locals import *
import sys
import random
from SimpleButton import *

# Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 400
FRAMERS_PER_SECOND = 30


# Define a function to be used as a "callback"
def myCallBackFunction():
    print('User Pressed B, called my myCallBackFunction')


# Define a class with a method to be used as a "callback"
class CallBackTest():
    def __init__(self):
        pass
    
    def myMethod(self):
        print('User pressed Button C, called myMethod of the CallBackTest object')


# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 Load assets: image(s), sounds, etc


# 5 Initialize the variables
oCallBackTest = CallBackTest()


oButtonA = SimpleButton(window, (25, 30),
                            'images/buttonAUp.png',
                            'images/buttonADown.png')

oButtonB = SimpleButton(window, (150, 30),
                            'images/buttonBUp.png',
                            'images/buttonBDown.png',
                            call_back=myCallBackFunction)

oButtonC = SimpleButton(window, (275, 30),
                            'images/buttonCUp.png',
                            'images/buttonCDown.png',
                            call_back=oCallBackTest.myMethod)

counter = 0


# Loop forever
while True:
    # Check for and handle events:
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Pass the event to the button, see if has been clicked on
        if oButtonA.handleEvent(event):
            print('User pressed button A, handled in the main loop')

        # oButtonB and OButtonC have callbacks,
        # no need to check result of these calls
        oButtonB.handleEvent(event)
        
        oButtonC.handleEvent(event)



    # 9 Do any 'per frame' actions
    counter = counter + 1


    # Clear the window before drawing it again
    window.fill(BLACK)

    # 10 Draw the window elements
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    # 11 Update the window
    pygame.display.update()

    # 12 Slow thing down a bit
    clock.tick(FRAMERS_PER_SECOND)
