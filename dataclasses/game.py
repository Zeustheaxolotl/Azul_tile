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

        # tile_circle = TileCircle(tile_bag)
        # tile_circle.draw_tiles_from_bag()

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
        """
        How many players are in this game
        :return: an integer indicating the number of players
        """
        return self.number_of_players

    def get_players(self):
        """
        Returns a list of players
        :return: A list of player objects
        """
        return self.players

    def add_player(self, name):
        """
        Add a player to the game
        :param name: A string indicating the number of players
        :return: a player object
        """
        player = Player(name)
        self.players.append(player)
        # self.number_of_players=len(self.players)
        return player

    def make_tilebag(self):
        """
        Initialize the tile bag
        :return: None
        """
        self.tile_bag.make_tiles()

    def make_tile_circles(self):
        """
        Create the right number of tile circles based on the number of players. Those tile circles will have
        tiles on them.

        :return: None
        """
        for x in range(2 * self.number_of_players + 1):
            new_circle = TileCircle(self.tile_bag)

            # print("HERE!!!")
            self.tile_circles.append(new_circle)
            self.tile_circles[x].draw_tiles_from_bag()
            #self.tile_circles

    def show_selected_tiles(self):
        """
        Have tiles connected to the mouse cursor shown on the screen.
        :return: None
        """
        offset_x = -15
        offset_y = -15
        for tile in self.selected_tiles:
            x, y = pygame.mouse.get_pos()
            tile.show(self.display, x + offset_x, y + offset_y)
            offset_x += 45

    def current_color(self):
        """
        Determine the color for the background screen based on the player
        :return: a tuple of numbers for
        """
        if self.current_player:
            return (self.current_player.player_color[0] / 5,
                    self.current_player.player_color[1] / 5,
                    self.current_player.player_color[2] / 5)
        return (0, 0, 0)

    def end_of_round(self):
        """
        This method is to do the various things that need to be done at the end of the round.
        For each player:
            * The tiles need to be moved to the tile wall
            * Released tiles need to be return to the tile_bag
            * release tiles from the overflow
            * Score calculation needs to be made
            * determination if the game is over
            * repopulate the tile circles


        :return:
        """
        # tiles need to be moved to the tile wall
        end_game = False
        for player in self.players:
            c_a = player.collection_area
            for i in range(len(c_a.tile_rows)):
                if c_a.tile_rows[i].is_full():
                    tiles = c_a.tile_rows[i].flush_tiles()
                    player.tilewall.add_tile(i, tiles[0])
                    del tiles[0]
                    self.tile_bag.tiles.append(tiles)
            overflow = player.overflow
            tiles = overflow.tilerow.flush_tiles()  # this should give back all the tiles that are not the 1st player tile.
            self.tile_bag.tiles.append(tiles)
           # player.add_to_score(player.tilewall.round_score())
           # end_game = end_game or player.tilewall.is_game_over()
        if end_game:
            # the game is over. Final calculations
            self.game.end_game()

        else:
            # time to repopulate the tile
            for circle in self.tile_circles:
                circle.draw_tiles_from_bag()
            # add the 1st player to the center circle

    def end_game(self):
        self.game_stage = GameStage.FINAL_SCREEN
        for player in self.players:
            #final_bonus = player.tilewall.calculate_final_bonus()
            player.add_to_score(final_bonus)

    def is_end_of_round(self):
        for circle in self.tile_circles:
            if not circle.is_empty():
                return False
        if not self.center_circle.is_empty():
            return False
        return True
