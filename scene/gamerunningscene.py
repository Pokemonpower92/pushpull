import sys

import pygame

from gamestate.eventhandler import EventHandler
from logger.pushpulllogger import PushPullLogger
from pushpullconfig import colors

from levels.mocklevel import MockLevel
from pushpullconstants.eventconstants import EventConstants
from pushpulltypes.tiletypes import TileTypes
from scene.scene import Scene
from sprite.playersprite.playersprite import PlayerSprite


class GameRunningScene(Scene):
    """
    This is the scene that runs the main game loop.
    """

    def __init__(self):
        super().__init__()
        self._non_player_sprites = pygame.sprite.Group()
        self._platform_sprites = pygame.sprite.Group()
        self._player_sprite = pygame.sprite.Group()
        self._level = MockLevel()
        self._load_resources()

    def _load_resources(self) -> None:
        """
        Load all the resources for the scene.
        :return: None
        """

        sprites = self._level.load_sprites()
        self._non_player_sprites.add(sprites[TileTypes.PLATFORM])
        self._platform_sprites.add(sprites[TileTypes.PLATFORM])
        self._all_sprites.add(sprites[TileTypes.PLATFORM])

        self.player = PlayerSprite(self._platform_sprites)
        self._all_sprites.add(self.player)

    def _update(self) -> None:
        """
        Update all the sprites in the scene.
        :return: None
        """
        try:
            player_events, global_events = EventHandler().get_events()

            if EventConstants.GAME_EXITED in global_events:
                self._logger.info("Game exited", 2)
                sys.exit()

            self._window.fill(colors.DARKGREY)

            for sprite in self._non_player_sprites:
                sprite.update()

            self.player.update(player_events)

            if not self.player.alive():
                self._logger.info("Player died", 2)
                sys.exit()

        except Exception as e:
            self._logger.error(f"Failed to update scene. Error: {e}", 2)
