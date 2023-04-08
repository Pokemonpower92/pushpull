import unittest

from levels.mocklevel import MockLevel


class TestTestLevel(unittest.TestCase):

    def setUp(self) -> None:
        self._level = MockLevel()

    def test_load_sprites(self):
        sprites = self._level.load_sprites()
        assert sprites
