from dataclasses.screens.numberplayersscreen import NumberPlayersScreen
from dataclasses.gamestage import GameStage
import pygame
import sys

white = (255, 255, 255)


class Game():
    ''''
    The Game class is here to organize the flow of the game.

    '''

    def __init__(self, display, screen_dim):
        self.game_stage = GameStage.NUMBER_OF_PLAYERS
        self.display = display
        self.screen_dim = screen_dim
        self.screens = {GameStage.NUMBER_OF_PLAYERS: NumberPlayersScreen(self)}

    def listen(self):
        self.screens[self.game_stage].listen()

    def show(self):
        self.screens[self.game_stage].show()

    def number_of_players(self):
        return self.number_of_players

    def players(self):
        return self.players
