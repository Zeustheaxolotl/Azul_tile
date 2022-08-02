import random
import pygame, sys
from tilebag import Tilebag
from pygame.locals import *


class TileCircle:
    def __init__(self, tile_bag: Tilebag):
        self.tile_bag = tile_bag
        self.tiles = []
        self.image = pygame.image.load('../img/tile_circle_200x200.png')

    def draw_tiles_from_bag(self, num=4):
        self.tiles.append(self.tile_bag.draw_tiles(num, "tile_circle"))

    def show(self, screen, x, y):
        screen.blit(self.image, (x, y))
        if len(self.tiles) == 1:
            screen.blit.self.tiles[1].show(screen, x + 100, y + 100)
            print(self.tiles[1])
        if len(self.tiles) == 2:
            screen.blit.self.tiles[1].show(screen, x + 40, y + 100)
            print(self.tiles[1])
            screen.blit.self.tiles[2].show(screen, x + 140, y + 100)
            print(self.tiles[2])
        if len(self.tiles) == 3:
            screen.blit.self.tiles[1].show(screen, x + 100, y + 40)
            print(self.tiles[1])
            screen.blit.self.tiles[2].show(screen, x + 40, y + 120)
            print(self.tiles[2])
            screen.blit.self.tiles[3].show(screen, x + 140, y + 120)
            print(self.tiles[3])
        if len(self.tiles) == 4:
            screen.blit.self.tiles[1].show(screen, x + 40, y + 40)
            print(self.tiles[1])
            screen.blit.self.tiles[2].show(screen, x + 40, y + 120)
            print(self.tiles[2])
            screen.blit.self.tiles[3].show(screen, x + 40, y + 120)
            print(self.tiles[3])
            screen.blit.self.tiles[4].show(screen, x + 140, y + 120)
            print(self.tiles[4])


if __name__ == "__main__":
    tile_bag = Tilebag()
    tile_bag.make_tiles()
    tile_circle = TileCircle(tile_bag)
    #tile_circle.draw_tiles_from_bag()

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
