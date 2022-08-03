import os
import sys

import pygame
from pygame.locals import *

from dataclasses.tilebag import Tilebag


class TileCircle:
    def __init__(self, my_tile_bag: Tilebag):
        self.tile_bag = my_tile_bag
        self.tiles = []
        self.image = pygame.image.load('img/tile_circle_200x200.png')

    def draw_tiles_from_bag(self, num=4):
        self.tiles = self.tile_bag.draw_tiles(num, "tile_circle")

    def show(self, screen, x, y):
        screen.blit(self.image, (x, y))
        if len(self.tiles) == 1:
            self.tiles[0].show(screen, x + 100, y + 100)
            # print(self.tiles[0])
        if len(self.tiles) == 2:
            self.tiles[1].show(screen, x + 40, y + 100)
            # print(self.tiles[1])
            self.tiles[0].show(screen, x + 140, y + 100)
            # print(self.tiles[0])
        if len(self.tiles) == 3:
            self.tiles[1].show(screen, x + 100, y + 40)
            # print(self.tiles[1])
            self.tiles[2].show(screen, x + 40, y + 120)
            # print(self.tiles[2])
            self.tiles[0].show(screen, x + 140, y + 120)
            # print(self.tiles[0])
        if len(self.tiles) == 4:
            self.tiles[1].show(screen, x + 40, y + 40)
            # print(self.tiles[1])
            self.tiles[2].show(screen, x + 140, y + 40)
            # print(self.tiles[2])
            self.tiles[3].show(screen, x + 40, y + 120)
            # print(self.tiles[3])
            self.tiles[0].show(screen, x + 140, y + 120)
            # print(self.tiles[0])


if __name__ == "__main__":
    os.chdir("../")  # this is to get the images to work
    tile_bag = Tilebag()
    tile_bag.make_tiles()
    tile_circle = TileCircle(tile_bag)
    # tile_circle.draw_tiles_from_bag()

    pygame.init()
    display = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Hello World!')
    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        tile_circle.show(display, 100, 50)
        pygame.display.update()
