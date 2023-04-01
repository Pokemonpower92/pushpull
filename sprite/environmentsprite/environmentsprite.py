from typing import Dict, Any

import pygame


class EnvironmentSprite(pygame.sprite.Sprite):
    """
    Environment sprites are all objects in the game that are part of the
    environment that are inert.

    ex: Walls, floors, backgrounds
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def custom_draw(self, window: pygame.surface) -> None:
        """
        Draw the environment sprite to the given window.
        :param window: The surface to draw the sprite on.
        :return: None
        """
        pass
