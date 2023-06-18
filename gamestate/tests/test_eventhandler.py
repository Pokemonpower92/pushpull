from unittest import TestCase, mock

import pygame

from gamestate.eventhandler import EventHandler
from pushpullconstants.eventconstants import EventConstants


class MockPygameEvent:

    def __init__(self, pygame_type, key=None):
        self.type = pygame_type
        self.key = key


class TestEventHandler(TestCase):

    def setUp(self) -> None:
        self.mock_pygame_events = [MockPygameEvent(pygame.KEYDOWN, pygame.K_SPACE),
                                   MockPygameEvent(pygame.KEYUP, pygame.K_SPACE), MockPygameEvent(pygame.QUIT)]
        self.mock_returned_player_evs = [EventConstants.JUMP_BUTTON_PRESSED, EventConstants.JUMP_BUTTON_RELEASED]
        self.mock_returned_global_evs = [EventConstants.GAME_EXITED]

    @mock.patch("pygame.event.get")
    def test_get_events(self, mock_events) -> None:
        """
        Ensure that EventHandler returns the appropriate
        Tuple of events.
        :return: None.
        """

        ev = EventHandler()

        mock_events.return_value = self.mock_pygame_events

        expected_values = self.mock_returned_player_evs, self.mock_returned_global_evs
        returned_evs = ev.get_events()

        for player_event in expected_values[0]:
            assert player_event in returned_evs[0]

        for global_event in expected_values[1]:
            assert global_event in returned_evs[1]
