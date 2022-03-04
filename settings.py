from math import pi, tan

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 120
TILE = 100
FPS_POS = (WIDTH - 50, 0)
ROWS, COLS = HEIGHT // TILE, WIDTH // TILE


# minimap settings
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, 0)


# ray casting settings
FOV = pi / 3  # угол обзора
HALF_FOV = FOV / 2
NUM_RAYS = 120  # кол-во лучей
MAX_DEPTH = 800  # дальность прорисовки
DELTA_ANGLE = FOV / NUM_RAYS  # угол между лучами
DIST = NUM_RAYS / (2 * tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# player settings
player_pos = (150, 150)
player_angle = 0
player_speed = 2

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220, 0, 0)
DARKGRAY = (110, 110, 110)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)
YELLOW = (220, 220, 0)