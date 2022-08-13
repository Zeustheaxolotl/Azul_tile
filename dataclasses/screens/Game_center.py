import pygame
from dataclasses.screens.screen import Screen, exit_check
import math
from dataclasses.tilecircle import TileCircle
from dataclasses.tilebag import Tilebag


class Game_Center(Screen):

    def __init__(self, game, circles, number_of_players):
        super().__init__(game)
        self.circles = circles
        self.number_of_players = number_of_players
        print('here')

    def reset_num_of_players(self, number_of_players):
        pass

    def show(self):

        self.display.fill((0, 0, 0))
        # print(self.players)
        for i in range(len(self.circles)):
            x = 500 + 300 * math.cos((2 * math.pi) / len(self.circles) * i)
            y = 300 + 300 * math.sin((2 * math.pi) / len(self.circles) * i)
            self.circles[i].show(self.display, x, y)

    def listen(self):
        for event in pygame.event.get():
            exit_check(event)


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
    GC_screen = Game_Center(display, tile_circle)
    while True:  # main game loop
        display.fill((0, 0, 0))
        TC_screen.show()
        TC_screen.listen()

        pygame.display.update()
