import pygame

from dataclasses.tilebag import Tilebag
from dataclasses.tilerow import TileRow
from dataclasses.screens.screen import exit_check


class CollectionArea:
    """
    The collection area is where player place tiles they pick up before the end of round.
    """

    def __init__(self, game):
        """
        The initialization of the Collection Area
        :param game: reference to the game for communication
        """
        self.game = game
        self.tile_rows = []
        self.create_tile_rows()

    def create_tile_rows(self):
        """
        Helper method when the collection area is initialized to create the rows.
        :return: None
        """
        for i in range(5):
            tile_row = TileRow(i + 1)
            self.tile_rows.append(tile_row)

    def show(self, screen, x, y):
        """
        Draw the Collection Area. Do this by drawing individual tile rows
        :param screen: A place to display the information
        :param x: the x-coordinate of the top left corner of the collection area
        :param y: The y-coordinate of the top left corner of the collection area
        :return: None
        """
        offset_y = 2
        for tile_row in self.tile_rows:
            tile_row.show(screen, x + 2, y + offset_y)
            offset_y += 36

    def listen(self, event):
        """
        Handle events and see if there was a click in the collection area
        :param event: a pygame event
        :return:
        """
        pass

    def end_of_round(self):
        """
        Clean up from the end of the round
        :return: Maybe the tiles that are to be returned to the tile_bag
        """
        pass


if __name__ == "__main__":

    tile_bag = Tilebag()
    tile_bag.make_tiles()
    collection_area = CollectionArea(None)
    new_tiles = tile_bag.draw_tiles(4, "Collection Area")
    collection_area.tile_rows[2].accept_tiles(new_tiles)
    pygame.init()
    display = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Collection Area Test')
    # TC_screen = Test_Tile_Circle_Screen(display, tile_circle)
    while True:  # main game loop
        display.fill((0, 0, 0))
        collection_area.show(display, 100, 100)
        for event in pygame.event.get():
            # if user types QUIT then the screen will close
            exit_check(event)

        # TC_screen.listen()

        pygame.display.update()