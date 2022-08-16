import random
import os
from dataclasses.tile import Tile


class Tilebag:
    def __init__(self):
        path = os.getcwd()
        path_parts = path.split("/")
        if path_parts[-1] == "dataclasses":
            os.chdir("../")
        print(os.getcwd())
        self.tiles = []
        self.colors = ['red', 'blue', 'yellow', 'black', 'teal']
        self.images = ['img/Red_Tile.png', 'img/Blue_Tile.png', 'img/Yellow_Tile.png',
                       'img/Black_Tile.png', 'img/Teal_Tile.png']

    def make_tiles(self):
        for x in range(len(self.colors)):
            for y in range(20):
                new_tile = Tile('tile bag', self.colors[x], self.images[x], y)
                self.tiles.append(new_tile)
                # print(new_tile.__str__())

    def draw_tiles(self, num, location):
        drawn_tiles = []
        # print('here')
        for z in range(num):
            i = random.randint(0, len(self.tiles))
            self.tiles[i].reset_location(location)
            drawn_tiles.append(self.tiles[i])
            # print(self.tiles[i].__str__())
            self.tiles.pop(i)
        return drawn_tiles

if __name__ == "__main__":
    new_tilebag = Tilebag()
    new_tilebag.make_tiles()
    new_tilebag.draw_tiles(4, "tile circle")
