import pygame

from scene.scene import Scene
from sprite.environmentsprite.platformsprite import PlatformSprite
from sprite.playersprite.playersprite import PlayerSprite


class GameRunningScene(Scene):
    """
    This is the scene that runs the main game loop.
    """

    def __init__(self):
        super().__init__()
        self._wall_sprites = pygame.sprite.Group()
        self._load_resources()

    def _load_resources(self) -> None:
        self._logger.info("Creating the floor sprite.", stacklevel=2)
        floor = PlatformSprite((0, 700), (1400, 100))
        self._all_sprites.add(floor)

        self._logger.info("Creating the player sprite.", stacklevel=2)
        player = PlayerSprite()
        self._all_sprites.add(player)
