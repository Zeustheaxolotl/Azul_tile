class Player():

    def __init__(self, name, next_player):
        self.name = name
        self.next_player = next_player
        self.score = 0

    def get_next_player(self):
        return self.next_player

    def score(self):
        return self.score

    def add_to_score(self, amount):
        self.score += amount
