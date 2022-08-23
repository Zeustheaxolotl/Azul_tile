from dataclasses.gamestage import GameStage
from dataclasses.player import Player
from dataclasses.screens.gamecenter import GameCenter
from dataclasses.screens.nameentry import NameEntry
from dataclasses.screens.numberplayersscreen import NumberPlayersScreen
from dataclasses.tilebag import Tilebag
from dataclasses.tilecircle import TileCircle
from dataclasses.screens.Playerboard_screen import Playerboard_screen
import pygame

white = (255, 255, 255)


class Game:
    """The Game class is here to organize the flow of the game."""

    def __init__(self, display, screen_dim):
        """
        The init method creates all the variables/methods that are necessary to play a game
        :param display: A display where the information will be displayed
        :param screen_dim: A tuple with the width and height of the display
        """
        self.number_of_players = None
        self.current_player = None
        self.players = []
        self.game_stage = GameStage.NUMBER_OF_PLAYERS
        self.display = display
        self.screen_dim = screen_dim
        self.tile_circles = []
        self.selected_tiles = []
        self.screens = {GameStage.NUMBER_OF_PLAYERS: NumberPlayersScreen(self),
                        GameStage.PLAYER_NAMES: NameEntry(self),
                        GameStage.GAME_CENTER: GameCenter(self),
                        GameStage.PLAYERBOARD_SCREEN: Playerboard_screen(self)}

        self.tile_bag = Tilebag()
        self.tile_bag.make_tiles()
        self.center_circle = TileCircle(self.tile_bag, type="blank")
        self.player_name_entry = 0

    def listen(self):
        """
        The listen method handles events.
        In general the game listen method passes off to the current screen listen method.

        :return: None
        """
        self.screens[self.game_stage].listen()

    def show(self):
        """
        The show method draws the screen. In general, it tries to draw based on the screen that is the current screen.

        :return: None
        """
        self.screens[self.game_stage].show()

    def get_number_of_players(self):
        return self.number_of_players

    def get_players(self):
        return self.players

    def add_player(self, name):
        player = Player(name)
        self.players.append(player)
        return player

    def make_tilebag(self):
        self.tile_bag.make_tiles()

    def make_tile_circles(self):
        for x in range(2 * self.number_of_players + 1):
            new_circle = TileCircle(self.tile_bag)

            # print("HERE!!!")
            self.tile_circles.append(new_circle)
            self.tile_circles[x].draw_tiles_from_bag()

    def show_selected_tiles(self):
        offset_x = -15
        offset_y = -15
        for tile in self.selected_tiles:
            x, y = pygame.mouse.get_pos()
            tile.show(self.display, x + offset_x, y + offset_y)
            offset_x += 45

    def current_color(self):
        if self.current_player:
            return (self.current_player.player_color[0] / 5,
                    self.current_player.player_color[1] / 5,
                    self.current_player.player_color[2] / 5)
        return (0, 0, 0)
