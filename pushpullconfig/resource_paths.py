import os

# Change to the root directory (./Garbage) from any file that
# imports resource_paths.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname + "/..")

TILES_PATH = os.path.abspath("resources/tiles")
PLATFORMS_PATH = TILES_PATH + "/platforms"
