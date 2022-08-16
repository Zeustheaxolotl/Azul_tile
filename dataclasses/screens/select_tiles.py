import pygame
from dataclasses.screens.screen import Screen, exit_check

class Select_Tiles(Screen):

    def __init__(self, game, circles):
        super().__init__(game)
        self.circles = circles

    def show(self):
        self.display.fill((0, 0, 0))

    def listen(self):
        for event in pygame.event.get():
            exit_check(event)
