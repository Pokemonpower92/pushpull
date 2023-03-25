from typing import Tuple, Dict, Any

import pygame

from pushpullconfig import colors
from sprite.environmentsprite.environmentsprite import EnvironmentSprite


class PlatformSprite(EnvironmentSprite):
    """
    Platform sprites are walls and floors.
    They have full blocking collision.
    """

    def __init__(self, position: Tuple, dimensions: Tuple):
        """
        Get s PlatformSprite
        :param dimensions: The dimensions of the platform sprite.
        :param position: The top-left coordinates of the platform sprite.
        """
        super().__init__()

        self._dimensions = dimensions
        self._position = position
        self._hit_box = None

        self.rect = None
        self.image = None

        self._load_assets({})

    def _load_assets(self, assets: Dict[str, Any]):
        self.image = pygame.Surface(self._dimensions)
        self.image.fill(colors.RED)
        self.rect = self.image.get_rect(topleft=self._position)
        self._hit_box = self.rect.inflate(.1, .1)
