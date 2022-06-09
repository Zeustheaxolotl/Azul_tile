import random


class TileCircle:
    def __init__(self, tile_bag):
        self.tile_bag=tile_bag
        self.tiles = []


    def calc_tiles(self):
        random.shuffle(self.tile_bag)
        for x in range(4):
            self.tiles.append(self.tile_bag[-1])
            del self.tile_bag[-1]
       #rnum = random.sample(range(0, len(tile_bag)), 4)
      # for z in rnum:
     #       rtile = tile_bag[z]
    #        rnums.append(z)
   #         del tile_bag[z]
  #          self.tiles.append(rtile)
#
#           print(self.tiles)
    def show(self):
        for x in range(4):
            print(self.tiles[x])

