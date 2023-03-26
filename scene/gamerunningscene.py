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
        floor = PlatformSprite((0, 750), (1400, 50))
        celing = PlatformSprite((0, 0), (1400, 50))
        left_wall = PlatformSprite((0, 50), (50, 1200))
        right_wall = PlatformSprite((1350, 50), (50, 1200))

        self._all_sprites.add(floor)
        self._wall_sprites.add(floor)
        self._all_sprites.add(celing)
        self._wall_sprites.add(celing)
        self._all_sprites.add(left_wall)
        self._wall_sprites.add(left_wall)
        self._all_sprites.add(right_wall)
        self._wall_sprites.add(right_wall)

        self._logger.info("Creating the player sprite.", stacklevel=2)
        player = PlayerSprite(self._wall_sprites)
        self._all_sprites.add(player)
