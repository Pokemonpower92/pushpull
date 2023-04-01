"""Holds json data for levels"""
from pushpulltypes.leveldatakeys import LevelDataKeys
from pushpullconfig import resourcepaths
from pushpulltypes.tiletypes import TileTypes

TEST_LEVEL_DATA = {
    LevelDataKeys.TILES: {
        TileTypes.PLATFORM: resourcepaths.PLATFORM_TILES_PATH + "/test_level.png",
    },
    LevelDataKeys.TILEMAPS: {
        TileTypes.PLATFORM: resourcepaths.PLATFORM_TILEMAPS_PATH + "/test_level.csv",
    },
    LevelDataKeys.INITIAL_PLAYER_POSITION: [100, 100]
}
