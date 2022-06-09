import random
from tilebag import TileBag

class TileCircle:
    def __init__(self, tile_bag: TileBag):
        self.tile_bag=tile_bag
        self.tiles = []


    def calc_tiles(self):
        #random.shuffle(self.tile_bag) # tile_bag does this automatically
        #for x in range(4):
        self.tiles.append(self.tile_bag.drawTiles(4))
            #del self.tile_bag[-1] # tile bag does this
       #rnum = random.sample(range(0, len(tile_bag)), 4)
      # for z in rnum:
     #       rtile = tile_bag[z]
    #        rnums.append(z)
   #         del tile_bag[z]
  #          self.tiles.append(rtile)
#
#           print(self.tiles)
    def show(self):
        for x in range(len(self.tiles)):
            print(self.tiles[x])

if __name__ == "__main__":
    tile_bag=TileBag()
    tile_bag.initialize()
    tile_circle=TileCircle(tile_bag)
    tile_circle.calc_tiles()
    tile_circle.show()
