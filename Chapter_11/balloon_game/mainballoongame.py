# Balloon game main code

# 1 - import packages
from pygame.locals import *
import pygwidgets
import sys
import pygame
from BalloonManager import *
from balloonconstants import *

# 2 Define constants
BLACK = (0,0,0)
# set up the constants
GRAY = (200, 200, 200)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30
BACKGROUND_COLOR = (0,255,255)


# set up the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

# 4 - Load assets image(s), sounds etc.
oScoreDisplay = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + 25),
                                        'Score: 0', textColor=BLACK,
                                        backgroundColor=None,
                                        width=140,
                                        fontSize=24)

oStatusDisplay = pygwidgets.DisplayText(window, (100, USABLE_WINDOW_HEIGHT + 25), '',
                                                 textColor=BLACK, backgroundColor=None)


oStartButton = pygwidgets.TextButton(window, (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10), 'Start')

# Initalize variables
oballoon_manager = BalloonManager(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)
playing = False # wait untill user clicks Start

# main loop
while True:
    # 7 check for handle events
    n_points_earned = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if playing:
            oballoon_manager.handle_event(event)
            the_score = oballoon_manager.get_score()
            oScoreDisplay.setValue("Score: " + str(the_score))
        elif oStartButton.handleEvent(event):
            oballoon_manager.start()
            oScoreDisplay.setValue("Score: 0 ")
            playing = True
            oStartButton.disable()

    if playing:
        oballoon_manager.update()
        n_popped = oballoon_manager.get_count_popped()
        n_missed = oballoon_manager.get_count_missed()
        oStatusDisplay.setValue('Popped: ' + str(n_popped) + 
                                ' Missed: ' + str(n_missed) + 
                                ' Out of: ' + str(N_BALLOONS))

        if (n_popped + n_missed) == N_BALLOONS:
            playing = False
            oStartButton.enable()

        

# 9 - Clear he window
    window.fill(BACKGROUND_COLOR)

    if playing:
        oballoon_manager.draw()
    
    pygame.draw.rect(window, GRAY, pygame.Rect(0, USABLE_WINDOW_HEIGHT, WINDOW_WIDTH, PANEL_HEIGHT))

    oScoreDisplay.draw()
    oStatusDisplay.draw()
    oStartButton.draw()


    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)

