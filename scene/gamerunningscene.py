import pygame

from levels.mocklevel import MockLevel
from pushpulltypes.tiletypes import TileTypes
from scene.scene import Scene
from sprite.playersprite.playersprite import PlayerSprite


class GameRunningScene(Scene):
    """
    This is the scene that runs the main game loop.
    """

    def __init__(self):
        super().__init__()
        self._platform_sprites = pygame.sprite.Group()
        self._level = MockLevel()
        self._load_resources()

    def _load_resources(self) -> None:
        """
        Load all the resources for the scene.
        :return: None
        """

        sprites = self._level.load_sprites()
        self._platform_sprites.add(sprites[TileTypes.PLATFORM])
        self._all_sprites.add(sprites[TileTypes.PLATFORM])

        player = PlayerSprite(self._platform_sprites)
        self._all_sprites.add(player)
