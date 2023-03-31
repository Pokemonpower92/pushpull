import unittest

from sprite.spritesheet import SpriteSheet
from pushpullconfig import resource_paths, gameconfig


class TestSpriteSheet(unittest.TestCase):

    def setUp(self) -> None:
        self._file = resource_paths.PLATFORMS_PATH + "/test_platforms.png"

    def test_get_offset_from_position(self):
        sheet = SpriteSheet(self._file, gameconfig.SPRITE_DIMENSIONS)

        offset = sheet._get_offset_from_position(7)
        assert offset == (32, 96)

        offset = sheet._get_offset_from_position(0)
        assert offset == (0, 0)


