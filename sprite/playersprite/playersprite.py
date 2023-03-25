from typing import Dict, Any

import pygame

from pushpullconfig import colors


class PlayerSprite(pygame.sprite.Sprite):
    """
    Player sprite is teh sprite for the player. Duh
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._dimensions = (20, 40)
        self._position = (20, 660)
        self._hit_box = None

        self.rect = None
        self.image = None

        self._load_assets({})

    def _load_assets(self, assets: Dict[str, Any]):
        """
        Load the assets for the sprite.
        :param assets: The assets to be loaded.
        :return: None
        """
        self.image = pygame.Surface(self._dimensions)
        self.image.fill(colors.GREEN)
        self.rect = self.image.get_rect(topleft=self._position)
        self._hit_box = self.rect.inflate(.1, .1)
