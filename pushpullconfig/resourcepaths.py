import os

# Change to the root directory (./Garbage) from any file that
# imports resource_paths.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname + "/..")

# Tilemaps.
TILEMAP_PATH = os.path.abspath("resources/tilemaps")
PLATFORM_TILEMAPS_PATH = TILEMAP_PATH + "/platforms"

# Sprite Sheets.
TILES_PATH = os.path.abspath("resources/tiles")
PLATFORM_TILES_PATH = TILES_PATH + "/platforms"
