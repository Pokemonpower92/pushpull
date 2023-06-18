from gamestate.window import Window
from logger.pushpulllogger import PushPullLogger
import pygame

from pushpullconfig.gameconfig import FPS


class Scene:
    """Scenes are the invokers for a particular scene to be displayed."""

    def __init__(self):
        self._window = Window().get_window()
        self._all_sprites = pygame.sprite.Group()
        self._running = False
        self._logger = PushPullLogger("scene")

        self._clock = pygame.time.Clock()

    def _update(self) -> None:
        """
        Update all the sprites in the scene.
        :return: None
        """
        pass

    def _load_resources(self) -> None:
        """
        Loads the resources for the scene.
        :return: None
        """
        pass

    def _draw_sprites(self) -> None:
        """
        Draw all the sprites in the scene.
        :return: None
        """
        try:
            self._all_sprites.draw(self._window)

        except Exception as e:
            self._logger.error(f"Failed to draw sprites for the scene. Error: {e}", 2)

    def run_scene(self) -> None:
        """
        Perform the game loop for the scene.
        :return:
        """

        try:
            self._running = True
            while self._running:
                self._clock.tick(FPS)
                self._update()
                self._draw_sprites()
                pygame.display.update()
                pygame.event.pump()

        except Exception as e:
            self._logger.error(f"Encountered error while running the scene. Error: {e}", 2)
