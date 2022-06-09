from enum import Enum

class TileColor(Enum):
    RED = 1
    BLACK = 2
    BLUE = 3
    TEAL=4
    YELLOW=5

class Tile:

    def __init__(self, location, color: TileColor):
        self.color = color #what kind is the tile
        self.location = location #where is the tile bag circle or playerboard

    def __str__(self):
        return str(self.color) + ", " + str(self.location) #say what color and where tile is

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.color==other.color

    # def re_tile_bag(self):
    #     if self.location == "tile bag":
    #         tile_bag.append(self.color)