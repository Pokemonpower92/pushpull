"""Configs for the player character not controlled by options."""
from pygame.math import Vector2

JUMPING_VELOCITY = Vector2(0, 5)
FALLING_VELOCITY = Vector2(0, -2)
WALKING_VELOCITY = Vector2(2, 0)
SPRINTING_VELOCITY = Vector2(5, 0)
VELOCITY_DECAY = Vector2(-2, -2)