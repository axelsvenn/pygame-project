from settings import *
from labyrinth import lab_map

text_map = lab_map()

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == "W":
            world_map.add((i * TILE, j * TILE))