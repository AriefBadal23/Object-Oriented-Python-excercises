# InputNumber class - allows the user to enter only numbers
# 
#  Demo of Inheritance

from unittest import result
import pygame
from pygame.locals import *
import pygwidgets

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Tuple of legal editing keys
LEGAL_KEYS_TUPLE = (pygame.K_RIGHT, pygame.KLEFT, pygame.K_HOME,
                    pygame.K_END, pygame.K_DELETE, pygame.K_BAKCSPACE,
                    pygame.K_RETURN, pygame.K_KP_ENTER)

# Legal keys to be typed
LEGAL_UNICODE_CHARS = ('0123456789')

# 
# InputNumber inherits from InputText
# 

class InputNumber(pygwidgets.InputText):
    """ Override the methods by inheriting of pygwidgets """

    def __init__(self, window, loc, value='', font_name=None,
                font_size=24, width=200, text_color=BLACK,
                background_color= WHITE, focus_color=BLACK,
                initial_focus= False, nick_name=None, callback=None,
                mask=None, keep_focus_onsubmit=False,
                # new parameters added
                allow_floating_number=True, allow_negative_number= True):
        self.allow_floating_number = allow_floating_number
        self.allow_negative_number = allow_negative_number

    
        super().__init__(window, loc, value, font_name, font_size,
        width, text_color, background_color, focus_color,
        initial_focus, nick_name, callback,
        mask, keep_focus_onsubmit)

    def handleEvent(self, event):
        if (event.type == pygame.KEYDOWN):
            # if it's not an editing or numeric key ignore it
            # unicode value is only present on key down'
            allowed_key = ((event.key in LEGAL_KEYS_TUPLE) or
                            (event.unicode in LEGAL_UNICODE_CHARS))
            if not allowed_key:
                return False

            if event.unicode == '-':
                if not self.allow_negative_number:
                    # if no negatives, dont pass through
                    return False
                if self.cursorPosition > 0:
                    return False # can't put minus sign after 1st char
                if '_' in self.text:
                    return False


            if event.unicode == '.':
                if not self.allow_floating_number:
                    # if no floats, dont pass the periode through
                    return False
                if '.' in self.text: # cant enter a second period
                    return False #cant enter a second period

            # Allow the key to go through to the base class
            result= super().handleEvent(event)
            return result

    def getValue(self):
        user_string = super().getValue()
        try:
            if self.allow_floating_number:
                return_value = float(user_string)
            else:
                return_value = int(user_string)
        except ValueError:
            raise ValueError('Entry is not a number, needs to have at least one digit.')
        return return_value