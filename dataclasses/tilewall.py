import pygame
from dataclasses.tilerow import TileRow
from dataclasses.tile import Tile


# from dataclasses.screens import screen


class Tile_Wall():
    def __init__(self):
        self.rect = None
        self.tiles = []
        self.image = pygame.image.load('img/Tile Wall.png')
        self.rows = []
        self.colors = ['blue', 'yellow', 'red', 'black', 'teal']
        self.create_tilerows()

    def create_tilerows(self):
        for i in range(5):
            tile_row = TileRow(5, "display")
            self.rows.append(tile_row)
        #for i in range(5):
            #new_tile = Tile('tile wall', 'black', 'img/Black_Tile.png', 101)
            #self.rows[i].display_tiles(new_tile, i)

    def show(self, screen, x, y):
        self.rect = screen.blit(self.image, (x, y))
        offset_y = 2
        for tile_row in self.rows:
            # print('here^^^^^')
            tile_row.show(screen, x + 2, y + offset_y)
            offset_y += 36

    def add_tile(self, row, tile):
        self.rows[row].display_tiles(tile, row)
    def round_score(self):
        pass
    def is_game_over(self):
        pass
    def calculate_final_bonus(self):
        pass
