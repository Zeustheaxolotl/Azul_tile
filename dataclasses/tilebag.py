from tile import TileColor, Tile
import random

class TileBag():

    def __init__(self):
        self.contents=[]

    def __repr__(self):
        return self.contents

    def __str__(self):
        ans=""
        for color in TileColor:
            ans+=str(color)+": "+str(self.contents.count(Tile("tile bag",color)))+"\n"
        return ans[:-1]

    def initialize(self):
        for color in TileColor:
            for x in range(0, 20, 1):
                new_tile = Tile("tile bag", color)
                self.contents.append(new_tile)

    def drawTiles(self, num=1):
        if num>len(self.contents):
            raise IndexError("Out of range of the tiles in the bag.")
        random.shuffle(self.contents)
        ans=self.contents[:num]
        del self.contents[:num]
        return ans

    def returnTiles(self, tiles):
        self.contents.append(tiles)

if __name__=="__main__":
    bag=TileBag()
    bag.initialize()
    print(str(bag))
    print(str(bag.drawTiles(4)))
    print(str(bag))