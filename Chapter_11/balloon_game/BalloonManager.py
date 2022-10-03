# Balloon Manager

import pygame
import random
from Balloon import Balloon_large, Balloon_medium, Balloon_small

from balloonconstants import BALLOONS_MISSED, N_BALLOONS

class BalloonManager():
    def __init__(self, window, max_width, max_height):
        self.window = window
        self.max_width = max_width
        self.max_height = max_height

    def start(self):
        """ Resets the count of popped balloons and the count of missed balloons
            I also creates new balloons.
        """
        self.balloon_list = []
        self.n_popped = 0
        self.n_missed = 0
        self.score = 0

        for balloon_num  in range(0, N_BALLOONS):
            
            random_balloon_class = random.choice((Balloon_small, Balloon_medium, Balloon_large))
            o_balloon = random_balloon_class(self.window, self.max_width, self.max_height, balloon_num)
            self.balloon_list.append(o_balloon)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Go 'reversed' so topmost balloon gets popped
            for o_balloon in reversed(self.balloon_list):
                was_hit, n_points = o_balloon.clicked_inside(event.pos)
                if was_hit:
                    if n_points > 0: # remove this balloon
                        self.balloon_list.remove(o_balloon)
                        self.n_popped = self.n_popped  + 1
                        self.score = self.score + n_points
                    return # no need to check others
        
        
    def update(self):
        """ Checks if a particular balloon has been clicked (popped) """
        for o_balloon in self.balloon_list:
            status = o_balloon.update()
            if status == BALLOONS_MISSED:
                # balloon went off the top, remove it
                self.balloon_list.remove(o_balloon)
                self.n_missed = self.n_missed + 1

    
    def get_score(self):
        return self.score

    def get_count_popped(self):
        return self.n_popped

    def get_count_missed(self):
        return self.n_missed

    def draw(self):
        for o_balloon in self.balloon_list:
            o_balloon.draw()
