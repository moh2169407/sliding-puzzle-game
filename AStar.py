from heapq import *
from Node import Node


class AI:
    def __init__(self, cells):
        self.cells = cells
        self.goal = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, None]
        ]

    def check_end(self, grid):
        flattened_grid = [cell.value if cell is not None else None for row in grid for cell in row]
        flattened_goal = [value for row in self.goal for value in row]
        return flattened_grid == flattened_goal

    def astar(self):
        open_list = []
        closed_set = set()
        heapify(open_list)
        initial_node = Node( None, self.cells, 0)
        heappush(open_list, initial_node)
        while open_list:
            current = heappop(open_list)
            if self.check_end(current.cells.grid) or current.h == 0:
                return self.reconstruct_path(current)
            if current in closed_set:
                continue
            children = current.generate_children(current.cells)
            for child in children:
                heappush(open_list, child)
            closed_set.add(current)
        return None

    def reconstruct_path(self, current):
        path = []
        while current:
            path.append(current.cells.grid)
            current = current.parent
        path.reverse()  # Reverse the path to show the solution from start to goal
        return path