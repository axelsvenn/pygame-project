import pygame
from settings import *
from map import world_map
from math import sin, cos


def mapping(x, y):
    return (x // TILE) * TILE, (y // TILE) * TILE


def ray_casting(sc, player_pos, player_angle):
    x0, y0 = player_pos
    xm, ym = (x0 // TILE) * TILE, (y0 // TILE) * TILE
    cur_angle = player_angle - HALF_FOV

    for ray in range(NUM_RAYS):
        sin_a = sin(cur_angle)
        cos_a = cos(cur_angle)

        # verticals
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE):
            depth_v = (x - x0) / cos_a
            y = y0 + depth_v * sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * TILE

        # horizontals
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, TILE):
            depth_h = (y - y0) / sin_a
            x = x0 + depth_h * cos_a
            if mapping(x, y + dy) in world_map:
                break
            y += dy * TILE

        # projects
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= cos(player_angle - cur_angle)
        proj_height = PROJ_COEFF / depth
        c = 255 / (1 + depth ** 2 * 0.00002)
        color = (c, c, c)
        pygame.draw.rect(sc, color,
                         (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

        cur_angle += DELTA_ANGLE