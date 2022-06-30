# Money example
# 
# Demonstrates overriding inherited DisplayText and InputText method

# 1 - Import Packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
from DisplayMoney import *
from InputNumber import *


# 2 - Define constants
BLACK = (0, 0, 0)
BLACKISH = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds, etc.
title = pygwidgets.DisplayText(window, (0, 40),
        'Demo of InputNumber and DisplayMoney fields',
        fontSize=36, width=WINDOW_WIDTH, justified='center')

input_caption = pygwidgets.DisplayText(window, (20, 150),
                'Input money amount', fontSize=24,
                width=190, justified='right')

inputField = InputNumber(window, (230, 150), '', width=150, initial_focus=True) 
ok_button = pygwidgets.TextButton(window, (430, 150), 'OK')


ouput_caption_1 = pygwidgets.DisplayText(window, (20, 300),
                    'Output dollars & cents:', fontSize=24,
                    width=190, justified='right')

money_field1 = DisplayMoney(window, (230, 300), '', textColor=BLACK,
                backgroundColor=WHITE, width=150)

ouput_caption_2 = pygwidgets.DisplayText(window, (20, 400),
                    'Output dollars only:', fontSize=24,
                    width=190, justified='right')

money_field2 = DisplayMoney(window, (230, 400), '', textColor=BLACK,
                backgroundColor=WHITE, width=150,
                showCents=False)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if inputField.handleEvent(event) or ok_button.handleEvent(event):
            try:
                theValue = inputField.getValue()
            except ValueError:
                inputField.setValue('(not a number)')
            else:
                the_text = str(theValue)
                money_field1.setValue(the_text)
                money_field2.setValue(the_text)

        window.fill(BACKGROUND_COLOR)

        title.draw()
        input_caption.draw()
        inputField.draw()
        ok_button.draw()
        ouput_caption_1.draw()
        money_field1.draw()
        ouput_caption_2.draw()
        money_field2.draw()
        
        pygame.display.update()

        clock.tick(FRAMES_PER_SECOND)