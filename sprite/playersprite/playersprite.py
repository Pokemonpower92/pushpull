import sys
from typing import Dict, Any

import pygame

from logger.pushpulllogger import PushPullLogger
from physics.physicsengine import PhysicsEngine
from pushpullconfig import colors
from pushpullconfig import playerconfig
from pushpulltypes.playeraction import PlayerAction


class PlayerSprite(pygame.sprite.Sprite):
    """
    Player sprite is teh sprite for the player. Duh
    """

    def __init__(self, obstructions: pygame.sprite.Group):
        pygame.sprite.Sprite.__init__(self)

        self.rect = None
        self.image = None
        self.direction = pygame.math.Vector2(0, 0)
        self.velocity = pygame.math.Vector2(0, 0)

        self._jump_count = playerconfig.NUM_JUMPS
        self._weight = 100
        self._physics_engine = PhysicsEngine()
        self._logger = PushPullLogger("playersprite")
        self._dimensions = (32, 32)
        self._position = (0, 576)
        self._hit_box = None
        self._obstructions = obstructions
        self._actions = [PlayerAction.IDLE]

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

    def _falling(self, rect) -> None:
        """
        Set the player to falling.
        :return: None
        """
        self.rect.top = rect.bottom
        self._hit_box.top = rect.bottom
        self.velocity.y = 0
        self.direction.y = -1

    def _landing(self, rect) -> None:
        """
        Set the player to grounded state.
        :return: None
        """
        self.velocity.y = 0
        self.rect.bottom = rect.top
        self._hit_box.bottom = rect.top
        self._jump_count = playerconfig.NUM_JUMPS

    def _check_vertical_collisions(self) -> None:
        """
        Check for any collisions on the y_axis.
        :return: None
        """

        self.rect.y += self.velocity.y
        for obj in self._obstructions:
            if obj.rect.colliderect(self.rect):
                # Check whether the player was rising or falling.
                if self.velocity.y < 0:
                    self._falling(obj.rect)
                else:
                    self._landing(obj.rect)

    def _check_horizontal_collisions(self) -> None:
        """
        Check for any collisions on the x_axis.
        :return: None
        """

        self.rect.x += self.velocity.x
        for obj in self._obstructions:
            if obj.rect.colliderect(self.rect):
                # Check whether the player was rising or falling.
                if self.velocity.x < 0:
                    self.rect.left = obj.rect.right
                    self._hit_box.left = obj.rect.right
                else:
                    self.rect.right = obj.rect.left
                    self._hit_box.right = obj.rect.left

                self.velocity.x = 0

    def _move(self) -> None:
        """
        Move the player the specified distance.
        :return: None
        """

        try:
            self._check_vertical_collisions()
            self._check_horizontal_collisions()

        except Exception as e:
            self._logger.error(f"Error moving player. {e}", 2)

    def _get_input(self) -> None:
        """
        Get input from the player and add it to the actions queue.
        :return: None
        """
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_SPACE]:
            self._actions.append(PlayerAction.JUMP)
        if pressed_keys[pygame.K_LSHIFT]:
            self._sprinting = True

        if pressed_keys[pygame.K_d]:
            self._actions.append(PlayerAction.MOVING_RIGHT)
        if pressed_keys[pygame.K_a]:
            self._actions.append(PlayerAction.MOVING_LEFT)

        if len(self._actions) == 0:
            self._actions.append(PlayerAction.IDLE)

        pygame.event.pump()

    def _take_action(self) -> None:
        """
        Take whatever actions are on the actions queue.
        :return: None
        """

        try:
            self.delta_velocity = pygame.math.Vector2(0, 0)

            while self._actions:
                action = self._actions.pop(0)
                if action == PlayerAction.MOVING_LEFT:
                    self.direction.x = -1
                    self.delta_velocity += playerconfig.WALKING_VELOCITY
                if action == PlayerAction.MOVING_RIGHT:
                    self.direction.x = 1
                    self.delta_velocity += playerconfig.WALKING_VELOCITY
                if action == PlayerAction.JUMP and self._jump_count > 0:
                    self.direction.y = -1
                    self.delta_velocity += playerconfig.JUMPING_VELOCITY
                    self._jump_count -= 1
                if action == PlayerAction.IDLE:
                    self.direction.y = 0

                self.velocity = self._physics_engine.calculate_velocity_for_frame(velocity=self.velocity,
                                                                                  delta_velocity=self.delta_velocity,
                                                                                  direction=self.direction)
                self._move()

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
