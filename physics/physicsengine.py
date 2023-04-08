import pygame.sprite
from pygame.math import Vector2
from logger.pushpulllogger import PushPullLogger
from pushpullconfig.gameconfig import FPS


class PhysicsEngine:
    """
    Makes physics calculations.
    """

    def __init__(self):
        self._logger = PushPullLogger("physicsengine")
        self._gravity = 3
        self._x_decay = 1
        self._terminal_velocity = Vector2(5, 30)

    def calculate_velocity_for_frame(self, **kwargs) -> Vector2:
        """
        Calculate the new velocity for the object in a given frame.
        :return: The calculated velocity.
        """
        original_velocity = kwargs.get("velocity")
        delta_velocity = kwargs.get("delta_velocity")
        direction = kwargs.get("direction")

        original_velocity.x = (delta_velocity.x * direction.x)
        original_velocity.y = (delta_velocity.y * direction.y)

        # Psudeo acceleration.
        original_velocity.y += self._gravity

        # Equal and opposite force or some shit.
        if original_velocity.x < 0:
            original_velocity.x += self._x_decay
        if original_velocity.x > 0:
            original_velocity.x -= self._x_decay

        return self._enforce_terminal_velocity(original_velocity)

    def _enforce_terminal_velocity(self, velocity: Vector2) -> Vector2:
        """
        Fix a velocity to be no greater than the terminal velocity.
        :param velocity: Vector of velocity to rectify
        :return: Rectified velocity.
        """

        if velocity.y < 0:
            velocity.y = max(self._terminal_velocity.y * -1, velocity.y)
        if velocity.y < 0:
            velocity.y = min(self._terminal_velocity.y, velocity.y)

        if velocity.x < 0:
            velocity.x = max(self._terminal_velocity.x * -1, velocity.x)
        if velocity.x < 0:
            velocity.x = min(self._terminal_velocity.x, velocity.x)

        return velocity
