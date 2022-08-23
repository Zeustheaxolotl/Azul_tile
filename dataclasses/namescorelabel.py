import pygame


class NameScoreLabel:

    def __init__(self, player):
        self.player = player

    def change_player(self, player):
        self.player = player

    def show(self, display, x, y):
        font_big = pygame.font.Font('freesansbold.ttf', 48)
        font_small = pygame.font.Font('freesansbold.ttf', 32)
        text_top_line = font_big.render(self.player.name, True, self.player.player_color)
        text_first_line = font_small.render("Score: " + str(self.player.get_score()), True, self.player.player_color)
        text_rect_top_line = text_top_line.get_rect(topleft=(x, y))
        text_rect_first_line = text_first_line.get_rect(topleft=(x, y + 50))
        display.blit(text_top_line, text_rect_top_line)
        display.blit(text_first_line, text_rect_first_line)
