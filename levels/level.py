from abc import abstractmethod
from typing import List
from csv import reader

from pushpulltypes.tiletypes import TileTypes


class Level:
    """
    Levels encapsulate all resources in a scene.
    """

    def __init__(self) -> None:
        self._tiles = {}
        self._sprites = {
            TileTypes.PLATFORM: []
        }
        self._level_data = None

    def _parse_csv(self, csv_file: str) -> List[int]:
        """
        Pull the 2 dimensional representation of a tilemap from
        its csv file.
        :param csv_file: Path to the CSV.
        :return: The tilemap as a 2d array.
        """
        tilemap = []

        with open(csv_file) as map:
            tile = reader(map, delimiter=",")
            for row in tile:
                tilemap.append(list(row))

        return tilemap

    @abstractmethod
    def load_sprites(self) -> None:
        """
        Load all the tiles for the level and store them in self._tiles.
        :return:
        """
        pass
