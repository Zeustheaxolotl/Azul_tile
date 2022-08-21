import math

import pygame

# from dataclasses.game import Game
#from dataclasses.game import Game
from dataclasses.gamestage import GameStage
from dataclasses.screens.screen import Screen, exit_check
from dataclasses.tilebag import Tilebag
from dataclasses.tilecircle import TileCircle
from dataclasses.scoretracker import ScoreTracker


class Game_Center(Screen):

    def __init__(self, game, circles, number_of_players):
        super().__init__(game)
        self.circles = circles
        self.number_of_players = number_of_players
        self.button_image = pygame.image.load('img/Azul Button.png')
        self.score_tracker = ScoreTracker(self.game.players, self.game.screen_dim)

        # print('here')

    def reset_num_of_players(self, number_of_players):
        pass

    def show(self):

        self.display.fill((0, 0, 0))
        self.score_tracker.show(self.display)
        # print(self.players)
        for i in range(len(self.circles)):
            x = 500 + 320 * math.cos((2 * math.pi) / len(self.circles) * i)
            y = 300 + 270 * math.sin((2 * math.pi) / len(self.circles) * i)
            self.circles[i].show(self.display, x, y)
        self.game.center_circle.show(self.display, 500, 300)
        self.game_center_button_rect = self.display.blit(self.button_image, (100, 700))

        # show selected tiles
        self.game.show_selected_tiles()

    def listen(self):
        for event in pygame.event.get():
            exit_check(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_center_button_rect.collidepoint(event.pos[0], event.pos[1]):
                    self.game.game_stage = GameStage.PLAYERBOARD_SCREEN
                    return None

                for circle in self.circles:
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
    pygame.display.set_caption('Tile Screen Test')
    game = Game(display, screen_dim)
    GC_screen = Game_Center(display, tile_circle, 3)
    while True:  # main game loop
        display.fill((0, 0, 0))
        GC_screen.show()
        GC_screen.listen()

        pygame.display.update()
