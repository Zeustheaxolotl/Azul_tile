from enum import Enum


class GameStage(Enum):
    """
    A class to keep track of what screen we are on.
    """
    NUMBER_OF_PLAYERS = 1
    PLAYER_NAMES = 2
    GAME_CENTER = 3
    ROUND_END = 4
