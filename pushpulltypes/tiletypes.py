from enum import Enum, unique


@unique
class TileTypes(Enum):
    """Cponstants for tile types present in levels."""
    PLATFORM = "platforms",
    PLAYER = "player"
