import pygame


class TileRow:

    def __init__(self, number_of_squares: int):
        """
        Initializer of the tile row
        :param number_of_squares: An integer representing the number of squares in the row
        """
        self.tiles = []
        self.tile_color = None
        self.number_of_squares = number_of_squares
        self.rect = None

    def show(self, screen, x, y):
        """
        The method to draw the row and tiles on the screen
        :param screen: The pygame display that the row will display on
        :param x: The upper left-hand corner x-coordinate
        :param y: The upper left-hand corner y-coordinate
        :return: None
        """
        # create a rectangle of space
        # place squares starting at the right end
        color = (200, 200, 200)
        for i in range(self.number_of_squares):
            pygame.draw.rect(screen, color, pygame.Rect(x + 2 + (4 - i) * 33, y + 1, 32, 32), 2)
            if i < len(self.tiles):
                self.tiles[i].show(screen, x + 2 + (4 - i) * 33, y + 1)
        self.rect = pygame.Rect(x + 2 + (5 - self.number_of_squares) * 33 + 2, y, 33 * self.number_of_squares + 4, 34)

    def accept_tiles(self, tiles):
        """
        Handler for adding new tiles to the row
        :param tiles: A list of tiles that need to go to the row
        :return: tiles that don't fit on the row.
        """
        if self.tile_color:
            if self.tile_color != tiles[0].color:
                raise ValueError("Wrong color.")
        else:
            self.tile_color = tiles[0].color
        squares_remaining = self.number_of_squares - len(self.tiles)
        # TODO: Look out for 1st player tile.
        if len(tiles) < squares_remaining:
            self.tiles += tiles
        else:
            self.tiles += tiles[:squares_remaining]
        return tiles[squares_remaining:]

    def flush_tiles(self):
        """
        Send tiles back
        :return: tiles on the row
        """
        old_tiles = list(self.tiles)
        self.tiles = []
        self.tile_color = None
        return old_tiles

    def is_full(self):
        """
        Test if the row is full
        :return: boolean that indicates if full
        """
        return self.number_of_squares == len(self.tiles)

    def collide_tile_row(self, x, y):
        """
        Is a coordinate inside the row.
        :param x:
        :param y:
        :return:
        """
        return self.rect.collidepoint(x, y)
