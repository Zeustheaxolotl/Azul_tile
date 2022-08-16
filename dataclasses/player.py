class Player:
    """
    A class to hold information about a player.
    """

    def __init__(self, name):
        self.name = name
        self.next_player = None
        self.score = 0

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

    def score(self):
        """
        Gets the score.
        :return: (int) the score
        """
        return self.score

    def add_to_score(self, amount):
        self.score += amount
