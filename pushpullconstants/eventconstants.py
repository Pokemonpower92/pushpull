from enum import unique, Enum


@unique
class EventConstants(Enum):
    # Constants for events
    GAME_EXITED = "game_exited"

    # These buttons need to be debounced so one event is processed
    # per button press.
    PAUSE_BUTTON_PRESSED = "pause_button_pressed"
    PAUSE_BUTTON_RELEASED = "pause_button_released"

    JUMP_BUTTON_PRESSED = "jump_button_pressed"
    JUMP_BUTTON_RELEASED = "jump_button_released"
