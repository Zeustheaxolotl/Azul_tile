import pygame
import sys


class Screen:

    def __init__(self, game):
        self.display = game.display
        self.screen_dim = game.screen_dim
        self.game = game

    def show(self):
        pass

    def listen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
