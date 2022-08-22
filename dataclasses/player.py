from dataclasses.collectionarea import CollectionArea


class Player:
    """
    A class to hold information about a player.

    There are two class variables. These are to make it so that each player has a different color.
    """
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    count = 0

    def __init__(self, name):
        self.name = name
        self.next_player = None
        self.score = 0
        self.player_color = Player.colors[Player.count % 4]
        Player.count += 1
        self.collection_area = CollectionArea()
        # self.overflow=Overflow()
        # self.tile_wall=TileWall()

    def add_next_player(self, player):
        """
        Give information about which player is next.
        :param player:
        :return: None
        """
        self.next_player = player

    def get_next_player(self):
        """
        Get the next player.
        :return: Player that comes next.
        """
        return self.next_player

    def get_score(self):
        """
        Gets the score.
        :return: (int) the score
        """
        return self.score

    def add_to_score(self, amount):
        """
        Change the current score of a player
        :param amount: The amount to increase the score
        :return: the adjusted the score of player
        """
        self.score += amount
        return self.score

    def show(self, display, x, y):
        """
        Show the player board setup  with a collection area, the tile wall and the overflow area
        :param display: The display that the player board is to be shown on
        :param x: The x coordinate of the upper left-hand corner
        :param y: The y coordinate of the upper left-hand corner
        :return: None
        """

        self.collection_area.show(display, x, y)
        # self.tile_wall(display, x+300, y)
        # self.overflow(display, x, y+400)


if __name__ == "__main__":
    play1 = Player("Bob")
    play2 = Player("Shirley")
    print(str(play1.player_color))
    print(str(play2.player_color))
