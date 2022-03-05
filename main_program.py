import pygame as pg
from settings import *
from player import Player
from drawing import Drawing


class App:
    def __init__(self):
        self.sc = pg.display.set_mode((WIDTH, HEIGHT))
        self.sc_map = pg.Surface((340, 340))
        self.clock = pg.time.Clock()
        self.player = Player()
        self.drawing = Drawing(self.sc, self.sc_map)

    def draw(self):
        self.sc.fill(BLACK)
        self.drawing.background()
        self.drawing.world(self.player.pos, self.player.angle)
        self.drawing.fps(self.clock)
        self.drawing.mini_map(self.player)

        pg.display.flip()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            self.player.movement()
            self.draw()
            self.clock.tick(FPS)


if __name__ == "__main__":
    pg.init()
    app = App()
    app.run()