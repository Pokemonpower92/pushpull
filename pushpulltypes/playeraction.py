from enum import Enum, unique

@unique
class PlayerAction(Enum):
    MOVING_LEFT = 0,
    MOVING_RIGHT = 1,
    JUMP = 2,
    IDLE = 3
