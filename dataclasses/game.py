from dataclasses.gamestage import GameStage
from dataclasses.player import Player
from dataclasses.screens.nameentry import NameEntry
from dataclasses.screens.numberplayersscreen import NumberPlayersScreen
from dataclasses.tilebag import Tilebag
from dataclasses.screens.Game_center import Game_Center

white = (255, 255, 255)


class Game:
    """The Game class is here to organize the flow of the game."""

    def __init__(self, display, screen_dim):
        self.number_of_players = None
        self.game_stage = GameStage.NUMBER_OF_PLAYERS
        self.display = display
        self.screen_dim = screen_dim
        self.tilecircles = []
        self.screens = {GameStage.NUMBER_OF_PLAYERS: NumberPlayersScreen(self),
                        GameStage.PLAYER_NAMES: NameEntry(self),
                        GameStage.GAME_CENTER: Game_Center(self, self.tilecircles, self.number_of_players)}
        self.players = []
        self.tile_bag = Tilebag()
        self.tile_bag.make_tiles()
        self.player_name_entry = 0
        # tile_circle = TileCircle(tile_bag)
        # tile_circle.draw_tiles_from_bag()

    def listen(self):
        self.screens[self.game_stage].listen()

    def show(self):
        self.screens[self.game_stage].show()

    def get_number_of_players(self):
        return self.number_of_players

    def get_players(self):
        return self.players

    def add_player(self, name):
        self.players.append(Player(name))

    def make_tilebag(self):
        self.tile_bag.make_tiles()

    def make_tilecircles(self):
        if self.number_of_players == 2:
            for x in range(5):
                new_circle = TileCircle(self.tile_bag)

                # print("HERE!!!")
                self.tilecircles.append(new_circle)
                self.tilecircles[x].draw_tiles_from_bag()

        elif self.number_of_players == 3:
            for x in range(7):
                new_circle = TileCircle(self.tile_bag)
                self.tilecircles.append(new_circle)
                self.tilecircles[x].draw_tiles_from_bag()

        elif self.number_of_players == 4:
            for x in range(9):
                new_circle = TileCircle(self.tile_bag)
                self.tilecircles.append(new_circle)
                self.tilecircles[x].draw_tiles_from_bag()
