from random import choice
from settings import *


class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {"top": True, "left": True, "right": True, "bottom": True}
        self.visited = False

    def check_cell(self, x, y):
        find_index = lambda x, y: x + y * COLS
        if x < 0 or x >= COLS or y < 0 or y >= ROWS:
            return False
        return grid_cells[find_index(x, y)]

    def check_neighbors(self):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False


def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False


grid_cells = [Cell(col, row) for row in range(ROWS)  for col in range(COLS)]


def lab_map():
    current_cell = grid_cells[0]
    stack = list()
    map_labyrinth = [["."] * 16 + ["."] for _ in range(ROWS * 2 + 1)]

    while not all(map(lambda c: c.visited, grid_cells)):
        current_cell.visited = True

        next_cell = current_cell.check_neighbors()
        if next_cell:
            next_cell.visited = True
            stack.append(current_cell)
            remove_walls(current_cell, next_cell)
            current_cell = next_cell

        elif stack:
            current_cell = stack.pop()

    for i in range(1, 16, 2):
        for j in range(1, 16, 2):
            map_labyrinth[j - 1][i - 1] = "W"
            map_labyrinth[j + 1][i + 1] = "W"
            current_cell = grid_cells[0].check_cell(i // 2, j // 2)

            if current_cell:
                cx, cy = current_cell.x * 2 + 1, current_cell.y * 2 + 1
                map_labyrinth[cy][cx + 1] = "W" if current_cell.walls["right"] else "."
                map_labyrinth[cy][cx - 1] = "W" if current_cell.walls["left"] else "."
                map_labyrinth[cy - 1][cx] = "W" if current_cell.walls["top"] else "."
                map_labyrinth[cy + 1][cx] = "W" if current_cell.walls["bottom"] else "."

    for i in range(len(map_labyrinth)):
        map_labyrinth[i][0] = "W"
        map_labyrinth[i][-1] = "W"

    return map_labyrinth

print(*map(lambda x: "".join(x), lab_map()), sep="\n")

if __name__ == "_main__":
    print(*map(lambda x: "".join(x), lab_map()), sep="\n")