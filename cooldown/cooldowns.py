from typing import Dict, Optional

import pygame

from cooldown.timer import Timer


class Cooldowns:
    """
    Cooldowns are an api for getting and setting cooldowns.
    """

    def __init__(self, cooldown_data: Optional[Dict[str, int]] = None):
        """
        Initialize the Cooldown
        :param cooldown_data:
        """
        self._cooldowns = {}

        if cooldown_data:
            self.set_cooldowns(cooldown_data)

    def set_cooldowns(self, cooldown_data: Optional[Dict[str, int]] = None) -> None:
        """
        Sets cooldowns for the instance from the cooldown data given.
        If a cooldown is already mapped it updates the timer to the one given.
        :param cooldown_data: Dictionary of cooldown timers keyed on cooldown name.
        :return: None
        """

        if cooldown_data:
            for cooldown, timer in cooldown_data.items():
                self._cooldowns[cooldown] = Timer(timer)

    def check_cooldown(self, cooldown: str) -> bool:
        """
        Check if the time elapsed has exceeded the timer given for the
        passed cooldown.
        :param cooldown: The name of the cooldown to check.
        :return: If the cooldown has expired.
        """
        return self._cooldowns[cooldown].check_timer()

    def reset_cooldown(self, cooldown: str) -> None:
        """
        Resets the given cooldown's internal timer.
        :param cooldown: The cooldown to reset.
        :return: None
        """
        self._cooldowns[cooldown].set_timer()
