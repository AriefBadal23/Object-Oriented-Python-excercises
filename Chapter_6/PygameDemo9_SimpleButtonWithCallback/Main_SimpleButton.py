# pygame demo 9 -3-button test witj callbacks

# 1 - Import packages
import pygame
from pygame.locals import *
from SimpleButton import *
import sys


# 2 - Define constants
GRAY = (200, 200, 200) 
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 60

# Define a function to be used as a "callback"
def my_call_back_function():
    print('User pressed Button B, called myCallBackfunction')



# Define a classs with a method to be useed as a "callback"
class Call_back_test():
    def __init__(self):
        pass

    def my_method(self):
        print('User pressed Button C, called my_method of the call_back_test object')



# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s),  etc.

# 5 - Initialize variables

oCallBackTest = Call_back_test()
# Create instances of SimpleButton
# No call back
oButtonA = SimpleButton(window, (25, 30),
                        'images/buttonAUp.png',
                        'images/buttonADown.png')

#Specifying a function to call back 
oButtonB = SimpleButton(window, (150, 30),
                        'images/buttonBUp.png',
                        'images/buttonBDown.png',
                        call_back=my_call_back_function)

# Specifying method to call back
oButtonC = SimpleButton(window, (275, 30),
                        'images/buttonCUp.png',
                        'images/buttonCDown.png',
                        call_back=oCallBackTest.my_method)

counter = 0

# 6 - Loop forever
while True:

     # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pass the event to the button, see if it has been clicked on
        if oButtonA.handleEvent(event):
            print("User has clicked the button A, handled in the main loop")

            # oButtonB and ObuttonC hadve callbacks,
            # no need to check result of these calss
            oButtonB.handleEvent(event)

            oButtonC.handleEvent(event)

    # 8 - Do any "per frame" actions
    counter= counter + 1

    # 9 - Clear the window
    window.fill(GRAY)

    # 10 - Draw all window elements
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()


    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait