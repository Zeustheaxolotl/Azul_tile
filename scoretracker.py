import pygame

from dataclasses.player import Player
from dataclasses.screens.screen import exit_check


class ScoreTracker:

    def __init__(self, players, dimensions):
        self.scores = {}
        self.players = players
        self.update_score()
        self.dimensions = dimensions
        self.width = dimensions[0] / 26
        self.height = dimensions[1] / 26

    def show(self, screen):
        self.update_score()
        color = (200, 200, 200)
        # right side
        for i in range(26):
            pygame.draw.rect(screen, color, pygame.Rect(0, self.dimensions[1] - (i + 1) * self.height,
                                                        self.width, self.height), 2)
        for i in range(1, 26):
            square = pygame.Rect((i) * self.width, 0, self.width, self.height)
            # print(square)
            pygame.draw.rect(screen, color, square, 2)
        for i in range(1, 26):
            square = pygame.Rect(self.dimensions[0] - self.width, i * self.height, self.width, self.height)
            # print(square)
            pygame.draw.rect(screen, color, square, 2)
        for i in range(1, 25):
            square = pygame.Rect(self.dimensions[0] - (i + 1) * self.width,
                                 self.dimensions[1] - self.height,
                                 self.width, self.height)
            pygame.draw.rect(screen, color, square, 2)

        for current_score in self.scores.keys():
            players = self.scores[current_score]

            current_score = current_score % 100
            offset = 0
            for player in players:
                width = self.width / len(players)
                if current_score <= 25:
                    marker = pygame.Rect(0 + offset * width, self.dimensions[1] - (current_score + 1) * self.height,
                                         width, self.height)
                    pygame.draw.rect(screen, player.player_color, marker)
                elif current_score <= 50:
                    marker = pygame.Rect((current_score - 25) * self.width + offset * width, 0,
                                         width, self.height)
                    pygame.draw.rect(screen, player.player_color, marker)
                elif current_score <= 75:
                    marker = pygame.Rect(self.dimensions[0] - self.width + offset * width,
                                         (current_score - 50) * self.height,
                                         width, self.height)
                    pygame.draw.rect(screen, player.player_color, marker)
                else:
                    marker = pygame.Rect(self.dimensions[0] - (current_score - 74) * self.width + offset * width,
                                         self.dimensions[1] - self.height,
                                         width, self.height)
                    pygame.draw.rect(screen, player.player_color, marker)
                offset += 1

    def update_score(self):
        self.scores = {}
        for player in self.players:
            if player.get_score() % 100 in self.scores.keys():
                self.scores[player.get_score() % 100].append(player)
            else:
                self.scores[player.get_score() % 100] = [player]


if __name__ == "__main__":

    pygame.init()
    display = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Score tracker Test')
    player1 = Player("Bob")
    player2 = Player("Shirley")
    player1.add_to_score(75)
    player2.add_to_score(76)
    st = ScoreTracker([player1, player2], (800, 600))
    while True:  # main game loop
        display.fill((0, 0, 0))
        for event in pygame.event.get():
            # if user types QUIT then the screen will close
            exit_check(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("HERE")
                    player1.add_to_score(1)
        st.show(display)
        # player1.add_to_score(1)
        # st.update_score()

        pygame.display.update()
