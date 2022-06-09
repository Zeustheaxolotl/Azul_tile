
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