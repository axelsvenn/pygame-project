from math import pi, tan

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 120
TILE = 100

# ray casting settings
FOV = pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 60
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# player settings
player_pos = (HALF_WIDTH, HALF_HEIGHT)
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