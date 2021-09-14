from enum import Enum


class GameInitiator(Enum):
    """
    Enum for game types.
    """
    PLAYER_1 = 1
    PLAYER_2 = 2
    RANDOM = 3


class Language(Enum):
    CPP = 1
    PYTHON = 2
    JAVA = 3


class Player():
    """
    Player class.
    """

    def __init__(self, language: Language):
        self.language = language


class Game:
    def __init__(
            self, initiator: GameInitiator, player1: Player, player2: Player):
        self.initiator = initiator
        self.player1 = player1
        self.player2 = player2
