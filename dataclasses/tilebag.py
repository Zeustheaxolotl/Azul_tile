import random
from dataclasses.tile import Tile


class Tilebag:
    def __init__(self):
        self.tiles = []
        self.colors = ['red', 'blue', 'yellow', 'black', 'teal']

    def make_tiles(self):
        for x in self.colors:
            for y in range(20):
                new_tile = Tile('tile bag', x)
                self.tiles.append(new_tile)
                #print(new_tile.__str__())

    def draw_tiles(self, num, location):
        drawn_tiles = []
        for z in range(num):
            i = random.randint(0, len(self.tiles))
            self.tiles[i].reset_location(location)
            drawn_tiles.append(self.tiles[i])
            #print(self.tiles[i].__str__())
            self.tiles.pop(i)
            return drawn_tiles




#new_tilebag = Tilebag()
#new_tilebag.make_tiles()
#new_tilebag.draw_tiles(4, "tile circle")


