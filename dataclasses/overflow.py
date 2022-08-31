import pygame
from dataclasses.tilerow import TileRow


class Overflow:
    def __init__(self):
        self.tilenum = 0
        # self.tiles = []
        self.score = 0
        self.oldtiles = []
        self.tilerow = TileRow(7, "overflow")

    def placeTile(self, tiles):
        self.tilerow.accept_tiles(tiles)
        self.tilenum += len(tiles)
        print(self.tilenum)

    '''def removeTile(self):
        self.tilenum = 0
        print(self.tilenum)
        self.tiles = []
        print(self.tiles)
        self.oldtiles = self.tiles
        return self.oldtiles '''

    def calc_score(self):
        if self.tilenum < 3:
            self.score = self.tilenum * -1
        elif self.tilenum < 6:
            self.score = (self.tilenum - 1) * -2
        elif self.tilenum == 6:
            self.score = -11
        else:
            self.score = -14
        print(self.score)

    def show(self, screen, x, y):
        """
        Draw the Collection Area. Do this by drawing individual tile rows
        :param screen: A place to display the information
        :param x: the x-coordinate of the top left corner of the collection area
        :param y: The y-coordinate of the top left corner of the collection area
        :return: None
        """
        offset_y = 2
        self.tilerow.show(screen, x + 2, y + offset_y)
        offset_y += 36

    def listen(self, event):
        """
        Handle events and see if there was a click in the collection area
        :param event: a pygame event
        :return:
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for tile_row in self.tile_rows:
                if tile_row.collide_tile_row(x, y):
                    return tile_row
                    # if not tile_row.is_full():
                    #    tile_row.accept_tiles(self.game.selected_tiles)
        return None


if __name__ == "__main__":
    prac = ['red', 'blue', 'yellow']
    prac1 = ['black', 'red', 'yellow', 'blue', 'teal']
    overflow_1 = Overflow()
    overflow_1.placeTile(prac)
    overflow_1.placeTile(prac1)
    overflow_1.calc_score()
    overflow_1.removeTile()
