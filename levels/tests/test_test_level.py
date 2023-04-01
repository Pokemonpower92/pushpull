import unittest

from levels.testlevel import TestLevel


class TestTestLevel(unittest.TestCase):

    def setUp(self) -> None:
        self._level = TestLevel()

    def test_load_sprites(self):
        sprites = self._level.load_sprites()
        assert sprites
