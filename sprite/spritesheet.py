from typing import Tuple

import pygame

from logger.pushpulllogger import PushPullLogger


class SpriteSheet:
    """
    SpriteSheet is a class that loads a sprite sheet,
    then parses it.
    """

    def __init__(self, filename: str, sprite_dimensions: Tuple[int, int]) -> None:
        """
        Initialize the SpriteSheet from the image in filename.
        :type dimensions: The dimensions of each sprite on the sheet.
        :param filename: filename of the image to load into the Sprite Sheet.
        """

        self._logger = PushPullLogger("spritesheet")

        try:
            self._sheet = pygame.image.load(filename)
            self._sheet_dimensions = (self._sheet.get_width(), self._sheet.get_height())
            self._sprite_dimensions = sprite_dimensions

            if self._sheet_dimensions[0] % self._sprite_dimensions[1]:
                raise Exception("sprite widths do not evenly divide the sheet width.")
            if self._sheet_dimensions[1] % self._sprite_dimensions[0]:
                raise Exception("sprite heights do not evenly divide the sheet height.")

        except Exception as e:
            self._logger.error(f"Error loading sprite sheet from file: {e}", 2)

    def _get_offset_from_position(self, position: int) -> Tuple[int, int]:
        """
        return the offset coordinates of the position from (0, 0) (top-left)
        :param position: The integer position.
        :return: The offset.
        """

        if position == 0:
            return 0, 0

        images_per_row = self._sheet_dimensions[0] // self._sprite_dimensions[0]
        images_per_col = self._sheet_dimensions[1] // self._sprite_dimensions[1]
        offset_x = (position // images_per_row) * self._sprite_dimensions[0]
        offset_y = (position % images_per_col) * self._sprite_dimensions[1]

        return offset_x, offset_y

    def get_image_at(self, position: int) -> pygame.image:
        """
        Get the image at a given position.
        SpriteSheet assumes the sprites are organized from right to left,
        top to bottom:
        0   1   2  ...  n
        n+1 n+2
        :param position: The integer position of the image to get.
        :return: the image loaded into a pygame.surface object.
        """
        image = pygame.Surface(self._sprite_dimensions)
        offset = self._get_offset_from_position(position)
        rect = pygame.Rect(offset[0], offset[1], self._sprite_dimensions[0], self._sprite_dimensions[1])
        image.blit(self._sheet, (0, 0), rect)

        return image
