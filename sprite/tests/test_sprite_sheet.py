import unittest

from sprite.spritesheet import SpriteSheet
from pushpullconfig import resourcepaths, gameconfig


class TestSpriteSheet(unittest.TestCase):

    def setUp(self) -> None:
        self._file = resourcepaths.PLATFORM_TILES_PATH + "/test_level.png"

    def test_get_offset_from_position(self):
        sheet = SpriteSheet(self._file, gameconfig.SPRITE_DIMENSIONS)

        offset = sheet._get_offset_from_position(7)
        assert offset == (32, 32)

        offset = sheet._get_offset_from_position(0)
        assert offset == (0, 0)

    def test_get_image_at(self):
        sheet = SpriteSheet(self._file, gameconfig.SPRITE_DIMENSIONS)

        for position in range(24):
            image = sheet.get_image_at(position)
