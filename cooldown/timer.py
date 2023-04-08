from pygame.time import get_ticks


class Timer:

    def __init__(self, time_limit: int) -> None:
        """
        Set the time limit and the reference.
        :param time_limit: The amount of ticks that need to pass for the timer to reset.
        """
        self._time_limit = time_limit
        self._time_reference = None
        self.set_timer()

    def set_timer(self) -> None:
        """
        Set the time reference.
        :return: None
        """
        self._time_reference = get_ticks()

    def check_timer(self) -> bool:
        """
        Check if the current ticks - time reference is greater than the time limit.
        :return: If the ticks elapsed since set_timer was called exceed the internal time limit.
        """
        return (get_ticks() - self._time_reference) > self._time_limit
