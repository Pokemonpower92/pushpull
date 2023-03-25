import pygame
from pushpullconfig import windowconfig
from logger.pushpulllogger import PushPullLogger

class Window:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Window, cls).__new__(cls)
            cls._window = get_window()
        return cls.instance

    def get_window(self):
        return self._window


def get_window():
    PushPullLogger("window").info(f"Creating window. Dims are: {windowconfig.WINDOW_DIMS}", 2)
    pygame.init()
    return pygame.display.set_mode(windowconfig.WINDOW_DIMS, 0, 32)