import pygame
from settings import *
from player import Player
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    sc.fill(BLACK)
    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)

    # pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
    # pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * cos(player.angle),
    #                                          player.y + HEIGHT * sin(player.angle)))
    #
    # for x, y in world_map:
    #     pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick(FPS)