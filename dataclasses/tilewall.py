import pygame
from dataclasses.tilerow import TileRow
from dataclasses.tile import Tile


# from dataclasses.screens import screen


class Tile_Wall():
    def __init__(self):
        self.rect = None
        self.image = pygame.image.load('img/Tile Wall.png')
        #self.tiles = [self.row1 == [None, None, None, None], self.row2 == [], self.row3 == [], self.row4 == [], self.row5 == []]
        self.rows = []
        self.colors = ['blue', 'yellow', 'red', 'black', 'teal']
        self.images = ['img/Blue_Tile.png', 'img/Yellow_Tile.png', 'img/Red_Tile.png', 'img/Black_Tile.png', 'img/Teal_Tile.png']
        self.create_tilerows()

    def create_tilerows(self):
        for i in range(5):
            tile_row = TileRow(5, "display")
            self.rows.append(tile_row)
        for i in range(4):
            new_tile = Tile('tile wall', self.colors[i], self.images[i], 101)
            self.rows[0].display_tiles(new_tile, 0)

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
        x = 0
        for row in self.rows:
            tiles = row.return_tiles()
            for tile in tiles:
                if tile:
                    x+=1
            if x == 5:
                print("game_is_over")
                return True
            else:
                print("game continues")
                return False

    def calculate_final_bonus(self):
        pass
