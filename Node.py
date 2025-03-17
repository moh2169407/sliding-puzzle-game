from copy import deepcopy
from Cells import Cells, Cell


class Node:
    def __init__(self, parent, cells, moves):
        self.parent = parent
        self.cells = cells
        self.moves = moves
        self.h = self.get_heuristic()
        self.f = self.h + self.moves

    def generate_children(self, cells):
        children = []
        for i in cells.get_neighbors():
            copy = deepcopy(cells)
            copy.move_cell(i)
            children.append(Node(self, copy, self.moves + 1))
        return children


    def get_heuristic(self):
        sum = 0
        for idx_row, val_row in enumerate(self.cells.grid):
            for idx_col, val_col in enumerate(val_row):
                if isinstance(val_col, Cell):
                    x = val_col.value  % 4
                    y = val_col.value // 4
                    sum += abs(x - idx_row) + abs(y - idx_col)

        return sum

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.cells.grid == other.cells.grid

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.cells.grid))