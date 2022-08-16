from dataclasses.screens.screen import Screen, exit_check
from dataclasses.gamestage import GameStage
import pygame


white = (255, 255, 255)


class NumberPlayersScreen(Screen):

    def __init__(self, game):
        super().__init__(game)

    def show(self):
        font_big = pygame.font.Font('freesansbold.ttf', 48)
        font_small = pygame.font.Font('freesansbold.ttf', 32)
        text_top_line = font_big.render('Number of Players?', True, white)
        text_first_line = font_small.render('2 players - press 2', True, white)
        text_second_line = font_small.render('3 players - press 3', True, white)
        text_third_line = font_small.render('4 players - press 4', True, white)
        text_rect_top_line = text_top_line.get_rect(center=(self.screen_dim[0] / 2, 300))
        text_rect_first_line = text_first_line.get_rect(center=(self.screen_dim[0] / 2, 350))
        text_rect_second_line = text_second_line.get_rect(center=(self.screen_dim[0] / 2, 390))
        text_rect_third_line = text_third_line.get_rect(center=(self.screen_dim[0] / 2, 430))

        self.display.blit(text_top_line, text_rect_top_line)
        self.display.blit(text_first_line, text_rect_first_line)
        self.display.blit(text_second_line, text_rect_second_line)
        self.display.blit(text_third_line, text_rect_third_line)

    def listen(self):
        for event in pygame.event.get():
            exit_check(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    print("2 players")
                    self.game.number_of_players = 2
                if event.key == pygame.K_3:
                    print("3 players")
                    self.game.number_of_players = 3
                if event.key == pygame.K_4:
                    print("4 players")
                    self.game.number_of_players = 4
                self.game.game_stage = GameStage.PLAYER_NAMES
                self.game.player_name_entry = 0
                self.game.make_tilebag()
                self.game.make_tile_circles()
