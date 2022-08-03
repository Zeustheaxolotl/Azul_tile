from abc import ABC, abstractmethod

from dataclasses.game import Game


class Screen(ABC):

    def __init__(self, game: Game):
        self.display = game.display
        self.screen_dim = game.screen_dim
        self.game = game

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def listen(self):
        pass
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #         sys.exit()
