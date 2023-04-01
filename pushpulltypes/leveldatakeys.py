from enum import Enum, unique


@unique
class LevelDataKeys(Enum):
    TILES = "tiles",
    TILEMAPS = "tilemaps",
    PLATFORM_TILES = "platform_tiles",
    PLATFORM_TILEMAP = "platform_tilemap",
    INITIAL_PLAYER_POSITION = "initial_player_position"
