import pygame


class TileRow:

    def __init__(self, number_of_squares: int, type):
        """
        Initializer of the tile row
        :param number_of_squares: An integer representing the number of squares in the row
        """
        self.tiles = []
        self.tile_color = None
        self.number_of_squares = number_of_squares
        self.rect = None
        self.type = type
        self.colors = ['blue','yellow','red','black','teal']
        if self.type == "display":
            self.tiles = [None, None, None, None, None]

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
            if self.type == "display":
                for i in range(5):
                    if self.tiles[i] is not None:
                        self.tiles[i].show(screen, (x-2-(4-i)*33)+135, y+1)
            else:
                if i < len(self.tiles):
                    self.tiles[i].show(screen, x + 2 + (4 - i) * 33, y + 1)
        self.rect = pygame.Rect(x + 2 + (5 - self.number_of_squares) * 33 + 2, y, 33 * self.number_of_squares + 4, 34)

    def accept_tiles(self, tiles):
        """
        Handler for adding new tiles to the row
        :param tiles: A list of tiles that need to go to the row
        :return: tiles that don't fit on the row.
        """
        overflow_tiles = []
        print(self.type)
        if self.type == "collect":
            print("HERE")
            if self.tile_color:
                print("here???")
                if self.tile_color != tiles[0].color and tiles[0].color != "first":
                    raise ValueError("Wrong color.")
            else:
                print("is it first" + tiles[0].color)
                if tiles[0].color == "first":
                    overflow_tiles = [tiles[0]]
                    del tiles[0]
                    print(tiles[0].color)
                self.tile_color = tiles[0].color
            squares_remaining = self.number_of_squares - len(self.tiles)
            if len(tiles) < squares_remaining:
                self.tiles += tiles
            else:
                self.tiles += tiles[:squares_remaining]
                for tile in tiles[squares_remaining:]:
                    overflow_tiles.append(tile)
            return overflow_tiles
        else:
            squares_remaining = self.number_of_squares - len(self.tiles)
            if len(tiles) < squares_remaining:
                self.tiles +=tiles

    def display_tiles(self, tile, row):
        if self.type == "display":
            for i in range(5):
                if tile.color == self.colors[i]:
                    print(row+i)
                    if row+i <= 4:
                        y = i + row
                        del self.tiles[y]
                        self.tiles.insert(y, tile)
                        #print(self.tiles)
                    else:
                        y = row-(5-i)
                        del self.tiles[y]
                        self.tiles.insert(y, tile)
                        #print(y)


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
