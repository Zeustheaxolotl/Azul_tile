class Player():

    def __init__(self, name):
        self.name = name
        self.next_player = None
        self.score = 0

    def add_next_player(self, player):
        self.next_player = player

    def get_next_player(self):
        return self.next_player

    def score(self):
        return self.score

    def add_to_score(self, amount):
        self.score += amount
