from typing import Tuple

import pygame

from pushpullconfig.keybinds import KeyBinds
from pushpullconstants.eventconstants import EventConstants


class EventHandler:
    """
    Top-level event handler.
    """

    def __init__(self):
        self._global_events = set()
        self._player_events = set()

    def get_events(self) -> Tuple:
        """
        Check for all events and return a
        Tuple containing player_events and global_events
        :return: player_events, global_events
        """

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self._global_events.add(EventConstants.GAME_EXITED)

            if event.type == pygame.KEYDOWN:
                if event.key == KeyBinds.PAUSE_BUTTON:
                    self._player_events.add(EventConstants.PAUSE_BUTTON_PRESSED)
                if event.key == KeyBinds.JUMP:
                    self._player_events.add(EventConstants.JUMP_BUTTON_PRESSED)

            if event.type == pygame.KEYUP:
                if event.key == KeyBinds.PAUSE_BUTTON:
                    self._player_events.add(EventConstants.PAUSE_BUTTON_RELEASED)
                if event.key == KeyBinds.JUMP:
                    self._player_events.add(EventConstants.JUMP_BUTTON_RELEASED)

        return self._player_events, self._global_events
