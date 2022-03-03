import pygame as pg
from settings import *
from player import Player
from drawing import Drawing


class App:
    def __init__(self):
        self.sc = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.player = Player()
        self.drawing = Drawing(self.sc)

    def draw(self):
        self.sc.fill(BLACK)
        self.drawing.background()
        self.drawing.world(self.player.pos, self.player.angle)
        self.drawing.fps(self.clock)

        pg.display.flip()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            self.player.movement()
            self.draw()
            self.clock.tick(FPS)


    # pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
    # pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * cos(player.angle),
    #                                          player.y + HEIGHT * sin(player.angle)))
    #
    # for x, y in world_map:
    #     pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)

if __name__ == "__main__":
    pg.init()
    app = App()
    app.run()