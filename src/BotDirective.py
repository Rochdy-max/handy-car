from enum import Enum

class BotDirective(Enum):
    NOTHING = 0 
    GO_FORWARD = 1
    GO_BACKWARD = 2
    TURN_LEFT = 3
    TURN_RIGHT = 4
    STOP = 5
