# Balloon game main code

# 1 - import packages
from pygame.locals import *
import pygwidgets
import sys
import pygame
from balloon_mngr import *
from balloonconstants import *

# 2 Define constants
BLACK = (0,0,0)
# set up the constants
GREY = (200, 200, 200)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30

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

oStatusDisplay = pygwidgets.DisplayText(window, (180, USABLE_WINDOW_HEIGHT + 25), '', textColor=BLACK, backgroundColor=None)


oStartButton = pygwidgets.TextButton(window, (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10), 'Start')


# Initalize variables
oballoon_manager = Balloon_mgr(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)
playing = False # wait unit user clicks Start

# main loop
while True:
    # 7 check for handle events
    n_points_earned = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if playing:
            oballoon_manager.handleEvent(event)
            the_score = oballoon_manager.get_score()
            oScoreDisplay.set_value("Score: " + str(the_score))
        elif oStartButton.handleEvent(event):
            oballoon_manager.start()
            oScoreDisplay.set_value("Score: " + str(the_score))
            playing = True
            oStartButton.disable()

    if playing:
        oballoon_manager.update()
        n_popped = oballoon_manager.get_count_popped()
        n_missed = oballoon_manager.get_count_missed()
        oStatusDisplay.setValue('Popped: ' + str(n_popped) +
                                ' Missed: ' + str(n_missed) +
                                'Out of: ' + str(N_BALLOONS))

        if (n_popped + n_missed) == N_BALLOONS:
            playing = False
            oStartButton.enable()
    
    # 9 - Clear he window
    window.fill(BACKGROUND_COLOR)

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)

