import math

import pygame

# from dataclasses.game import Game
# from dataclasses.game import Game
from dataclasses.gamestage import GameStage
from dataclasses.screens.screen import Screen, exit_check
from dataclasses.tilebag import Tilebag
from dataclasses.tilecircle import TileCircle
from dataclasses.scoretracker import ScoreTracker
from dataclasses.namescorelabel import NameScoreLabel


class GameCenter(Screen):

    def __init__(self, game):
        super().__init__(game)
        # self.circles = circles
        # self.number_of_players = number_of_players
        self.game = game
        self.button_image = pygame.image.load('img/Azul Button.png')
        self.score_tracker = ScoreTracker(self.game.players, self.game.screen_dim)
        self.name_label = NameScoreLabel(self.game.current_player)

        # print('here')

    def reset_num_of_players(self, number_of_players):
        pass

    def show(self):
        current_color = self.game.current_color()
        self.display.fill(current_color)
        self.score_tracker.show(self.display)
        # print(self.players)
        for i in range(len(self.game.tile_circles)):
            x = 500 + 320 * math.cos((2 * math.pi) / len(self.game.tile_circles) * i)
            y = 300 + 270 * math.sin((2 * math.pi) / len(self.game.tile_circles) * i)
            self.game.tile_circles[i].show(self.display, x, y)
        self.game.center_circle.show(self.display, 500, 300)
        self.name_label.change_player(self.game.current_player)
        self.name_label.show(self.display, 100, 600)
        self.game_center_button_rect = self.display.blit(self.button_image, (100, 700))

        # show selected tiles
        self.game.show_selected_tiles()

    def listen(self):
        # TODO: Fix how tiles return ot the circle. Have circle remember the old version of the tile, and reinstate it when the tiles are returned.
        for event in pygame.event.get():
            exit_check(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_center_button_rect.collidepoint(event.pos[0], event.pos[1]):
                    self.game.game_stage = GameStage.PLAYERBOARD_SCREEN
                    return None

                center_tiles = self.game.center_circle.get_clicked_tiles(event)
                if center_tiles:
                    self.game.selected_tiles = center_tiles[0]
                else:
                    # check the circles
                    for circle in self.game.tile_circles:
                        tiles = circle.get_clicked_tiles(event)
                        if tiles and len(self.game.selected_tiles) == 0:
                            self.game.selected_tiles += tiles[0]
                            self.game.center_circle.tiles += tiles[1]
                            self.game.last_tiles_rejected = tiles[1]
                            self.game.last_circle_tapped = circle
                        else:
                            if len(self.game.selected_tiles) > 0:
                                if circle == self.game.last_circle_tapped:
                                    # check that this is the circle that was selected last?
                                    circle.tiles = self.game.selected_tiles + self.game.last_tiles_rejected
                                    self.game.selected_tiles = []
                                    for tile in self.game.last_tiles_rejected:
                                        self.game.center_circle.tiles.remove(tile)
                                    self.game.last_tiles_rejected = []


if __name__ == "__main__":
    # os.chdir("../")  # this is to get the images to work
    # print(os.getcwd())
    tile_bag = Tilebag()
    tile_bag.make_tiles()
    tile_circle = TileCircle(tile_bag)
    tile_circle.draw_tiles_from_bag()

    pygame.init()
    screen_dim = (1200, 800)
    display = pygame.display.set_mode(screen_dim)
    pygame.display.set_caption('Game Center Test')
    # game = Game(display, screen_dim)
    GC_screen = GameCenter(None)
    while True:  # main game loop
        display.fill((0, 0, 0))
        GC_screen.show()
        GC_screen.listen()

        pygame.display.update()
