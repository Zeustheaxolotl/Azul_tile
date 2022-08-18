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
        self.score += amount


if __name__ == "__main__":
    x = Player("Bob")
    y = Player("Shirley")
    print(str(x.player_color))
    print(str(y.player_color))
