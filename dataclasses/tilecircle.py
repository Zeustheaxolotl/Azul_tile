import os
import sys

import pygame
from pygame.locals import *

from dataclasses.tilebag import Tilebag
from dataclasses.screens.screen import Screen, exit_check


class TileCircle:
    def __init__(self, my_tile_bag: Tilebag):
        self.tile_bag = my_tile_bag
        self.tiles = []
        self.image = pygame.image.load('img/tile_circle_200x200.png')
        self.rect = None

    def draw_tiles_from_bag(self, num=4):
        self.tiles = self.tile_bag.draw_tiles(num, "tile_circle")

    def show(self, screen, x, y):
        self.rect = screen.blit(self.image, (x, y))
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

    def collide_tiles(self, x, y):
        for tile in self.tiles:
            if tile.collide_tile(x, y):
                return tile
        return None

    def collide_tile_circle(self, x, y):
        return self.rect.collidepoint(x, y)


class Test_Tile_Circle_Screen(Screen):

    def __init__(self, screen, tile_circle):
        self.display = screen
        # self.screen_dim = game.screen_dim
        # self.game = game
        self.tile_circle = tile_circle
        self.tiles = []

    def show(self):
        # print("here")
        self.tile_circle.show(self.display, 400, 300)
        for tile in self.tiles:
            x, y = pygame.mouse.get_pos()
            tile.show(self.display, x - 15, y - 15)

    def listen(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                print(event.pos)
                x, y = event.pos
                hit_circle = self.tile_circle.collide_tile_circle(x, y)
                hit_tile = self.tile_circle.collide_tiles(x, y)
                if hit_circle and len(self.tiles) == 1:
                    self.tiles[0].location = "tile circle"
                    self.tile_circle.tiles.append(self.tiles[0])
                    self.tiles.clear()

                if hit_tile and len(self.tiles) < 1:
                    print(hit_tile)
                    self.tile_circle.tiles.remove(hit_tile)
                    hit_tile.location = "chosen"
                    self.tiles.append(hit_tile)




if __name__ == "__main__":
    # os.chdir("../")  # this is to get the images to work
    print(os.getcwd())
    tile_bag = Tilebag()
    tile_bag.make_tiles()
    tile_circle = TileCircle(tile_bag)
    tile_circle.draw_tiles_from_bag()

    pygame.init()
    display = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Tile Screen Test')
    TC_screen = Test_Tile_Circle_Screen(display, tile_circle)
    while True:  # main game loop
        display.fill((0, 0, 0))
        TC_screen.show()
        TC_screen.listen()

        pygame.display.update()
