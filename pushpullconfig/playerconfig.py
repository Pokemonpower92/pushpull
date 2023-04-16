"""Configs for the player character not controlled by options."""
from pygame.math import Vector2
from pushpullconstants.playerconstants import JUMP_COOLDOWN

# Stats
BASE_HEALTH = 100
BASE_ARMOR = 25

# Movement
JUMPING_VELOCITY = Vector2(0, 10)
FALLING_VELOCITY = Vector2(0, -2)
WALKING_VELOCITY = Vector2(5, 0)
SPRINTING_VELOCITY = Vector2(5, 0)

# Abilities
NUM_JUMPS = 2

COOLDOWNS = {
    JUMP_COOLDOWN: 500
}
