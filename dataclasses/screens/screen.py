import sys
from abc import ABC, abstractmethod

import pygame

from dataclasses.game import Game


def exit_check(my_event):
    if my_event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


class Screen(ABC):

    def __init__(self, game: Game):
        self.display = game.display
        self.screen_dim = game.screen_dim
        self.game = game

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def listen(self):
        pass
