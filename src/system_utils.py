# variables allowed to be accessed
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

game_state = None


# classes for system variables
from enum import (
    Enum
)

class GameState(Enum):
    LOADING = 1
    MAIN_LOOP = 2
    WON = 3
    QUITTING = 4
