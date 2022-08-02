from enum import Enum

class TileColor(Enum):
    RED = 1
    BLACK = 2
    BLUE = 3
    TEAL=4
    YELLOW=5


class Tile:

    def __init__(self, location, color):
        self.color = color
        # what kind is the tile
        self.location = location
        # where is the tile bag circle or player board

    def __str__(self):
        return self.color + ", " + self.location=-0[],
        # say what color and where tile is

    def show(self):
        pass

    class Tile:

        def __init__(self, location, color):
            self.color = color
            # what kind is the tile
            self.location = location
            # where is the tile bag circle or player board

        def __str__(self):
            return self.color + ", " + self.location
            # say what color and where tile is

        def show(self):
            pass

        def reset_location(self, new_location):
            self.location = new_location

        def __eq__(self, other):
            return self.color==other.color

        # def re_tile_bag(self):
        #     if self.location == "tile bag":
        #         tile_bag.append(self.color)