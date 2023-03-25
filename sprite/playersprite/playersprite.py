from typing import Dict, Any

import pygame

from logger.pushpulllogger import PushPullLogger
from physics.player_physics import PhysicsEngine
from pushpullconfig import colors
from pushpullconfig import playerconfig
from pushpulltypes.playeraction import PlayerAction


class PlayerSprite(pygame.sprite.Sprite):
    """
    Player sprite is teh sprite for the player. Duh
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._action = PlayerAction.IDLE
        self._direction = pygame.math.Vector2(0, 0)
        self._velocity = pygame.math.Vector2(0, 0)
        self._weight = 100

        self._dimensions = (20, 40)
        self._position = (20, 660)
        self._hit_box = None

        self.rect = None
        self.image = None

        self._logger = PushPullLogger("playersprite")
        self._physics_engine = PhysicsEngine()

        self._load_assets({})

    def _load_assets(self, assets: Dict[str, Any]):
        """
        Load the assets for the sprite.
        :param assets: The assets to be loaded.
        :return: None
        """

        try:
            self.image = pygame.Surface(self._dimensions)
            self.image.fill(colors.GREEN)
            self.rect = self.image.get_rect(topleft=self._position)
            self._hit_box = self.rect.inflate(.1, .1)
        except Exception as e:
            self._logger.error(f"Exception loading assets for player sprite. ERROR: {e}", 2)

    def _move(self, distance: pygame.math.Vector2) -> None:
        """
        Move the player the specified distance.
        :param distance: A vector describing the distance to move.
        :return: None
        """
        self.rect.x += distance.x
        self.rect.y += distance.y
        self._hit_box.x += distance.x
        self._hit_box.y += distance.y

    def _get_input(self) -> None:
        """
        Get input from the player and pick an action.
        :return: None
        """
        pressed_keys = pygame.key.get_pressed()

        # If the player doesn't press a key we want the
        # sprite to be idle.
        self._action = PlayerAction.IDLE

        if pressed_keys[pygame.K_SPACE]:
            self._action = PlayerAction.JUMP
        if pressed_keys[pygame.K_LSHIFT]:
            self._sprinting = True

        if pressed_keys[pygame.K_d]:
            self._action = PlayerAction.MOVING_RIGHT
        if pressed_keys[pygame.K_a]:
            self._action = PlayerAction.MOVING_LEFT

        pygame.event.pump()

    def _take_action(self) -> None:
        """
        Take whatever action derived from input is specified.
        :return: None
        """
        try:
            self._logger.info(f"Player took action: {self._action.name}", 2)
            added_velocity = pygame.math.Vector2(0, 0)

            if self._action == PlayerAction.MOVING_LEFT:
                self._direction = pygame.math.Vector2(-1, 0)
                added_velocity += playerconfig.WALKING_VELOCITY
            if self._action == PlayerAction.MOVING_RIGHT:
                self._direction = pygame.math.Vector2(1, 0)
                added_velocity += playerconfig.WALKING_VELOCITY
            if self._action == PlayerAction.JUMP:
                self._direction = pygame.math.Vector2(0, -1)
                added_velocity += playerconfig.JUMPING_VELOCITY
            if self._action == PlayerAction.IDLE:
                self._direction = pygame.math.Vector2(0, 0)
                added_velocity += playerconfig.VELOCITY_DECAY

            distance = self._physics_engine.calculate_distance(self._direction, self._velocity, added_velocity)
            self._move(distance)


        except Exception as e:
            self._logger.error(f"Exception taking player action. ERROR: {e}", 2)

    def _update_image(self) -> None:
        """
        Update the sprite's current image in the animation.
        :return: None
        """
        pass

    def update(self) -> None:
        """
        Update the player sprite.
        :return: None
        """

        try:
            self._get_input()
            self._take_action()
            self._update_image()

        except Exception as e:
            self._logger.error(f"Exception updating player sprite. ERROR: {e}", 2)




