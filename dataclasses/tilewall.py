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
        self.column_1 = 0
        self.column_2 = 0
        self.column_3 = 0
        self.column_4 = 0
        self.column_5 = 0
        self.columns = [self.column_1, self.column_2, self.column_3, self.column_4, self.column_5]
        self.score=0

    def create_tilerows(self):
        for i in range(5):
            tile_row = TileRow(5, "display")
            self.rows.append(tile_row)
        #for i in range(4):
            #new_tile = Tile('tile wall', self.colors[i], self.images[i], 101)
            #self.rows[4-i].display_tiles(new_tile, 4-i)
           # self.rows[0].display_tiles(new_tile, 0)

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
                #print(self.score)
                return True
            else:
                #print(self.score)
                return False

    def calculate_final_bonus(self):
        for row in self.rows:
            x = 0
            tiles = row.return_tiles()
            for tile in tiles:
                if tile:
                    x += 1
            if x == 5:
                self.score+=2
            for i in range(len(tiles)):
                if tiles[i]:
                    self.columns[i] += 1
        for column in self.columns:
            if column == 5:
                self.score += 10
        print('what is the score???? '+str(self.score))
        return self.score







