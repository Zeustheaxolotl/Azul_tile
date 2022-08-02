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
