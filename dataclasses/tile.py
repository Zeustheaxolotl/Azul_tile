from enum import Enum
import pygame
import os
import sys


class TileColor(Enum):
    RED = 1
    BLACK = 2
    BLUE = 3
    TEAL=4
    YELLOW=5


class Tile:

    def __init__(self, location, color, image):
        self.color = color
        # what kind is the tile
        self.location = location
        # where is the tile bag circle or player board
        self.image = pygame.image.load(image)

    def __str__(self):
        return self.color + ", " + self.location
        # say what color and where tile is

    def __eq__(self, other):
        return self.color == other.color

    def reset_location(self, new_location):
            self.location = new_location

    def show(self, screen, x, y):
        screen.blit(self.image, (x, y))

if __name__ == "__main__":
    #tile_bag = Tilebag()
    #tile_bag.make_tiles()
    os.chdir("../")  # find the images
    tile=Tile("nowhere","blue", "img/Blue_Tile.png")
    #tile_circle = TileCircle(tile_bag)
    #tile_circle.draw_tiles_from_bag()

    pygame.init()
    display = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Hello World!')
    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        tile.show(display, 100, 50)
        pygame.display.update()