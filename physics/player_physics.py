from pygame.math import Vector2
from logger.pushpulllogger import PushPullLogger


class PhysicsEngine:
    """
    Makes physics calculations.
    """

    def __init__(self):
        self._logger = PushPullLogger("physicsengine")

    def calculate_distance(self, direction: Vector2, original_velocity: Vector2, delta_velocity: Vector2) -> Vector2:
        """
        Move
        :param direction: Direction of the movement
        :param original_velocity: Object's original velocity
        :param delta_velocity: Change in velocity
        :return: The calculated distance traveled.
        """
        delta_velocity.x *= direction.x
        delta_velocity.y *= direction.y

        return original_velocity + delta_velocity

