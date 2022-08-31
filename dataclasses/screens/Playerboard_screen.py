import pygame

from dataclasses.gamestage import GameStage
from dataclasses.namescorelabel import NameScoreLabel
from dataclasses.overflow import Overflow
#import math
#from dataclasses.tilecircle import TileCircle
#from dataclasses.tilebag import Tilebag
#from main import game
from dataclasses.screens.screen import Screen, exit_check



class Playerboard_screen(Screen):

    def __init__(self, game):
        super().__init__(game)
        self.button_image = pygame.image.load('img/Azul Button.png')
        self.name_label = NameScoreLabel(None)
        self.current_color = (0, 0, 0)

    # self.circles = circles
    # self.number_of_players = number_of_players
    # self.button_image = pygame.image.load('img/Azul Button.png')
    # print('here')
    def change_player(self):

        self.name_label.change_player(self.game.current_player)
        self.current_color = self.game.current_color()

    def show(self):
        self.change_player()
        self.display.fill(self.current_color)
        # print(self.players)
        self.name_label.show(self.display, 600, 20)
        self.game.current_player.show(self.display, 100, 100)
        self.display.blit(self.button_image, (100, 700))
        self.game.show_selected_tiles()

    def listen(self):
        for event in pygame.event.get():
            exit_check(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 105 <= pygame.mouse.get_pos()[0] <= 165 and 705 <= pygame.mouse.get_pos()[1] <= 750:
                    self.game.game_stage = GameStage.GAME_CENTER

                type, obj = self.game.current_player.listen(event)
                if type == "row":
                    if not obj.is_full():
                        try:

                            overflow = obj.accept_tiles(self.game.selected_tiles)
                            self.game.current_player.place_overflow(overflow)
                            # TODO place overflow in the overflow area
                            self.game.selected_tiles = []
                            #print(self.game.current_player.get_next_player().name)
                            if self.game.is_end_of_round():
                                self.game.end_of_round()
                            else:
                                self.game.current_player = self.game.current_player.get_next_player()
                                self.game.game_stage = GameStage.GAME_CENTER

                        except ValueError:
                            print("wrong color")
