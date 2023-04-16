# Health Types

This page is the drawing board for the types of health
in pushpull.

## Vitality

Vitality is the primary health meter in the game.
Every destructable has some amount of health, even if just
a single hit point. When this is reduced to zero the destructable
is destroyed. Modification to vitality, positive or negative is
not given any modifier; a hit for 10 deals 10 damage to vitality,
and a heal for 10 restores 10 vitality.

## Armor

Armor is one of the secondary health meters. It is resistant to
physical damage, and provides mitigation to it in addition to being
a secondary health bar against physical damage. Armor provides a 25%
reduction in physical damage dealt from any source. Any amount of armor
will block any amount of physical damage; if a destructable has 10 armor
and a physical damage calculation for 50 occurs, the destructable's armor
is reduced to 0 but the remaining 25 damage in the calculation is avoided.

## Will

Will is the other secondary health meter. It provides mitigation, but not
protection from magical damage. Will is a augmentable percentage or magical
damage mitigation that is degraded by use. If a destructable has 100 will,
it will reduce incoming magical damage by 100% but is then reduced by
the amount of magical damage mitigated. For instance:

- The player has 75 Will.
- The player has 50 magical damage incoming.
- The player takes 12.5 damage from the attack (50 * (1 - 75/100))
- The player's Will takes 50 damage itself.
- The player is left with 25 Will.

