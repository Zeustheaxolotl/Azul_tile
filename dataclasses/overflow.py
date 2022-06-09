class Overflow():
    def __init__(self):
        self.tilenum=0
        self.tiles=[]
        self.score=0
        self.oldtiles = []
    def placeTile(self, tiles):
        for x in range(len(tiles)):
            self.tiles.append(tiles[x])
        self.tilenum += len(tiles)
        print(self.tilenum)
        print(self.tiles)

    def removeTile(self):
        self.tilenum=0
        print(self.tilenum)
        self.tiles = []
        print(self.tiles)
        self.oldtiles = self.tiles
        return self.oldtiles


    def calc_score(self):
        if self.tilenum < 3:
            self.score = self.tilenum*-1
        elif self.tilenum < 6:
            self.score = (self.tilenum-1)*-2
        elif self.tilenum == 6:
            self.score = -11
        else:
            self.score = -14
        print(self.score)

if __name__=="__main__":
    prac=['red', 'blue', 'yellow']
    prac1 = [ 'black', 'red','yellow', 'blue', 'teal']
    overflow_1= Overflow()
    overflow_1.placeTile(prac)
    overflow_1.placeTile(prac1)
    overflow_1.calc_score()
    overflow_1.removeTile()
