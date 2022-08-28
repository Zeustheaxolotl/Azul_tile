
import sys
import random

import pygame
from pygame.locals import *
from dataclasses.tilebag import Tilebag
from dataclasses.screens.screen import Screen, exit_check


class TileCircle:
    def __init__(self, my_tile_bag: Tilebag, type="disk"):
        self.tile_bag = my_tile_bag
        self.tiles = []
        self.image = pygame.image.load('img/tile_circle_200x200.png')
        self.rect = None
        self.type = type
        self.first = True
        self.positions = [(80, 0), (40, 40), (80, 40), (120, 40), (0, 80), (40, 80), (80, 80), (120, 80), (160, 80),
                          (40, 120), (80, 120), (120, 120), (80, 160)]
        if self.type == "blank":
            self.positions += [(0, 0), (40, 0), (120, 0), (160, 0), (0, 40), (160, 40), (0, 120), (160, 120),
                               (0, 160), (40, 160), (120, 160), (160, 160)]
            self.rect = pygame.Rect(500, 300, 200, 200)
            #print('get first tile')
            self.first_tile = self.tile_bag.get_first_tile('center')
            self.tiles.append(self.first_tile)

    def draw_tiles_from_bag(self, num=4):
        self.tiles = self.tile_bag.draw_tiles(num, "tile_circle")

    def show(self, screen, x, y):
        if self.type == "disk":
            self.rect = screen.blit(self.image, (x, y))
        for tile in self.tiles:
            if not tile.offset:
                offset = random.sample(self.positions, 1)
                tile.set_offset(offset[0])
                self.positions.remove(offset[0])
            tile.show(screen, x, y)

    def collide_tiles(self, x, y):
        for tile in self.tiles:
            if tile.collide_tile(x, y):
                return tile
        return None

    def collide_tile_circle(self, x, y):
        return self.rect.collidepoint(x, y)

    def get_clicked_tiles(self, event):
        """

        :param event: A pygame event

        :return: Tuple with tiles matching the clicked tiles and the rest of the tiles
        """
        if event.type == MOUSEBUTTONDOWN:
            # print(event.pos)
            x, y = event.pos
            # print(str(event.pos))
            if self.collide_tile_circle(x, y):  # hit the circle
                hit_tile = self.collide_tiles(x, y)# Was a tile hit?

                if hit_tile:
                    matching_tiles = []
                    unmatching_tiles = []
                    for tile in self.tiles:
                        print(tile.color)
                        if tile.color == hit_tile.color:
                            matching_tiles.append(tile)
                            self.positions.append(tile.offset)
                            tile.set_offset(None)
                        elif self.type != "blank":
                            unmatching_tiles.append(tile)
                            self.positions.append(tile.offset)
                            tile.set_offset(None)
                        elif self.type == "blank":
                            if tile.color == 'first':
                                matching_tiles.append(tile)
                                self.positions.append(tile.offset)

                                tile.set_offset(None)

                    if self.type == "blank":
                        #print(matching_tiles[0])
                        for tile in matching_tiles:
                            self.tiles.remove(tile)
                    else:
                        self.tiles = []
                    return (matching_tiles, unmatching_tiles)
        return None


class Test_Tile_Circle_Screen(Screen):

    def __init__(self, screen, tile_circle):
        self.display = screen
        # self.screen_dim = game.screen_dim
        # self.game = game
        self.tile_circle = tile_circle
        self.tiles = []
        self.center_tiles = []

    def show(self):
        # print("here")
        self.tile_circle.show(self.display, 400, 300)
        offset_x = -15
        offset_y = -15
        for tile in self.tiles:
            x, y = pygame.mouse.get_pos()
            tile.show(self.display, x + offset_x, y + offset_y)
            offset_x += 45

        x = 100
        y = 100
        offset_x = 0
        offset_y = 0
        for tile in self.center_tiles:
            tile.show(self.display, x + offset_x, y + offset_y)
            offset_x += 45
            if offset_x > 150:
                offset_y += 45
                offset_x = 0

    def listen(self):
        for event in pygame.event.get():
            exit_check(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                tiles = self.tile_circle.get_clicked_tiles(event)

                if tiles:
                    self.tiles += tiles[0]
                    self.center_tiles += tiles[1]
                else:
                    self.tile_circle.tiles = self.tiles + self.center_tiles
                    self.center_tiles = []
                    self.tiles = []


if __name__ == "__main__":
    # os.chdir("../")  # this is to get the images to work
    # print(os.getcwd())
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
