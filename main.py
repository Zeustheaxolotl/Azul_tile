# coding=utf-8
# This is a sample Python script.
import random
#from random import sample

#ran = random.sample(range(0, 99), 36)
#print(ran)
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
tile_bag = []
total_tiles = []
colors = ['red', 'black', 'blue', 'teal', 'yellow']
rnums = []
turn = 0
round = 0
row = False


class Tile:

    def __init__(self, location, color):
        self.color = color #what kind is the tile
        self.location = location #where is the tile bag circle or playerboard

    def __str__(self):
        return self.color + ", " + self.location #say what color and where tile is

    def __repr__(self):
        return str(self)

    def re_tile_bag(self):
        if self.location == "tile bag":
            tile_bag.append(self.color)


class TileCircle:
    def __init__(self, tiles):
        self.tiles = tiles


    def calc_tiles(self):
        random.shuffle(tile_bag)
        for z
       #rnum = random.sample(range(0, len(tile_bag)), 4)
      # for z in rnum:
     #       rtile = tile_bag[z]
    #        rnums.append(z)
   #         del tile_bag[z]
  #          self.tiles.append(rtile)
#
#           print(self.tiles)


for y in colors:
    for x in range(0, 20, 1):
        new_tile = Tile("tile bag", y)
        total_tiles.append(new_tile)

for x in range(0, 100, 1):
    total_tiles[x].re_tile_bag()

print(tile_bag)
TileCircles = []



