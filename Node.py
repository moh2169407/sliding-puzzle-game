import copy


class Node:
    def __init__(self, grid, parent, moves, pos):
        self.grid = grid
        self.parent = parent
        self.moves = moves
        self.move_pos = pos
        self.h = self.get_heuristic()
        self.f = self.h + self.moves

    # The heuristic is the manhattan distance, the amount of jumps to reach
    # the position where it should be
    def get_heuristic(self):
        sum = 0
        for row, i in enumerate(self.grid):
            for col, j in enumerate(i):
                if j is None:
                    continue
                val_row = (j - 1) // 4
                val_col = (j - 1) % 4
                sum += abs(row - val_row) + abs(col - val_col)
        return sum
    # Returns the blank location in the grid
    def blank_idx(self):
        idx = 0
        for i in self.grid:
            for e in i:
                if e is None:
                    return idx
                idx += 1

    # Finds all the neighbors, possible moves that can be made
    def get_neighbors(self):
        # Gets the pos of the blank
        blank_index = self.blank_idx()
        # Finds the row and col from the pos
        row = blank_index // 4
        col = blank_index % 4

        # List of all neighbors
        neighbors = []

        # list of possible moves

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for move in moves:
            r = row + move[0]
            c = col + move[1]
            # Checks to see if the moves is valid
            if 0 <= r < 4 and 0 <= c < 4:
                new_index = r * 4 + c
                neighbors.append(new_index)
        return neighbors
    # Generate children uses get_neighbor, and creates a new node after every move
    def generate_children(self):
        return_list = []
        for n in self.get_neighbors():
            row1 = self.blank_idx() // 4
            col1 = self.blank_idx() % 4
            new_grid = copy.deepcopy(self.grid)
            row = n // 4
            col = n % 4
            new_grid[row][col],new_grid[row1][col1] = new_grid[row1][col1], new_grid[row][col]
            return_list.append(Node(new_grid, self, self.moves, n))

        return return_list

    def __lt__(self, other):
        if self.f == other.f:
            return self.h < other.h  # Prefer lower h if f is the same
        return self.f < other.f