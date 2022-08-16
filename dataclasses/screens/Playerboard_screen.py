import pygame

from dataclasses.gamestage import GameStage
from dataclasses.screens.screen import Screen, exit_check
#import math
#from dataclasses.tilecircle import TileCircle
#from dataclasses.tilebag import Tilebag
#from main import game


class Playerboard_screen(Screen):

    def __init__(self, game):
        super().__init__(game)
        self.button_image = pygame.image.load('img/Azul Button.png')

       # self.circles = circles
       # self.number_of_players = number_of_players
       # self.button_image = pygame.image.load('img/Azul Button.png')
        # print('here')

    def show(self):

        self.display.fill((0, 0, 0))
        # print(self.players)
        self.display.blit(self.button_image, (100, 700))
        self.game.show_selected_tiles()



    def listen(self):
        for event in pygame.event.get():
            exit_check(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 105 <= pygame.mouse.get_pos()[0] <= 165 and 705 <= pygame.mouse.get_pos()[1] <= 750:
                    self.game.game_stage = GameStage.GAME_CENTER