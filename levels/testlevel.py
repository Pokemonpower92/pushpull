from typing import Dict

import pygame

from levels.level import Level
from logger.pushpulllogger import PushPullLogger
from pushpullconfig.leveldata import TEST_LEVEL_DATA
from pushpullconfig.gameconfig import SPRITE_DIMENSIONS
from pushpulltypes.leveldatakeys import LevelDataKeys
from pushpulltypes.tiletypes import TileTypes
from sprite.environmentsprite.platformsprite import PlatformSprite
from sprite.spritesheet import SpriteSheet


class TestLevel(Level):

    def __init__(self) -> None:
        super().__init__()
        self._logger = PushPullLogger("test_level")
        self._level_data = TEST_LEVEL_DATA

    def load_sprites(self) -> Dict[TileTypes, pygame.sprite.Sprite]:
        """
        Load all the tiles for the test level.
        :return: The dictionary of sprites.
        """

        try:
            tiles = self._level_data[LevelDataKeys.TILES]
            tilemaps = self._level_data[LevelDataKeys.TILEMAPS]

            for tile_type, csv_file in tilemaps.items():
                tilemap = self._parse_csv(csv_file)
                sprite_sheet = SpriteSheet(tiles[tile_type], SPRITE_DIMENSIONS)

                for row_index, row in enumerate(tilemap):
                    for col_index, sprite_sheet_position in enumerate(row):
                        sprite_sheet_position = int(sprite_sheet_position)
                        if sprite_sheet_position != -1:
                            sprite_position = (col_index * SPRITE_DIMENSIONS[0], row_index * SPRITE_DIMENSIONS[1])

                            image = sprite_sheet.get_image_at(sprite_sheet_position)

                            if tile_type == TileTypes.PLATFORM:
                                self._sprites[tile_type].append(
                                    PlatformSprite(sprite_position, SPRITE_DIMENSIONS, image))

        except Exception as e:
            self._logger.error(f"Error loading sprites: {e}", 2)

        return self._sprites
