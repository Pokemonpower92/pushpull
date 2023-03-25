import sys

import pygame

from logger.pushpulllogger import PushPullLogger


class EventHandler:
    """
    Top-level event handler.
    """

    @staticmethod
    def check_for_exit_event() -> None:
        """
        Checks for someone exiting the game.
        :return: None
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PushPullLogger("eventhandler").info("Exiting the game.", 2)
                sys.exit()

