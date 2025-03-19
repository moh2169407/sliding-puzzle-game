from operator import truediv

import pygame as pg
from pygame.examples.stars import move_stars
import random

# Constants
# Colors
WHITE = (255, 255, 255)
GRAY = (187, 187, 187)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 300, 350
RED = (255, 0, 0)

class Cell:
    # Value is the number to be printed
    # Pos is the (1-16) possible position on the board
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos

    def draw(self, surface):
        # The coordinates for the Cell
        x, y = 0, 0
        # The width and height of the cell, 4x4
        w2, h2 = WIDTH / 4, HEIGHT / 4
        # Calculates the x,y position based on the 2-dimensional array
        if 0 <= self.pos <= 3:
            x = self.pos * w2
            y = 0
        elif 4 <= self.pos <= 7:
           x = self.pos * w2 - 300
           y = h2
        elif 8 <= self.pos <= 11:
            x = self.pos * w2 - 600
            y = h2 * 2
        elif 12 <= self.pos <= 15:
            x = self.pos * w2 - 900
            y = h2 * 3

        # Creates a new font
        font = pg.font.Font(None, 30)
        text = font.render(f'{self.value}', False, BLACK)
        text_rect = text.get_rect()
        # Centers the text inside the middle of the box
        text_rect.center = (x + 37, y + 43)
        # Creates a new box and a white outline
        pg.draw.rect(surface, WHITE, (x, y, w2, h2))
        pg.draw.rect(surface, GRAY, (x, y, w2, h2), 1)
        # Draws the text
        surface.blit(text, text_rect)

    def change_pos(self, pos):
        self.pos = pos


class Cells:
    def __init__(self):
        # The total moves made
        self.moves = 0
        # The 2D grid
        self.grid = [[None for i in range(4)] for i in range(4)]
        # Creates a solved grid, and shuffles to generate a solvable grid
        for i in range(1, 16):
            cell = Cell(i, i - 1)
            self.add_value(cell)
        self.add_value(None)


        # Shuffles the grid 1000 times
        for i in range(1000):
            neighbor = self.get_neighbors()
            choice = random.choice(neighbor)
            self.move_cell(choice)


    # Initiates the grid
    def add_value(self, cell):
        for c in range(4):
            for r in range(4):
                # Checks to see if the current pos is empty
                if self.grid[c][r] is None:
                    self.grid[c][r] = cell
                    return

    def draw(self, surface):
        surface.fill(BLACK) # Clears the screen
        for col in self.grid:
            for row in col:
                # Draws the cell
                if isinstance(row, Cell):
                    row.draw(surface)

    def get_index(self, val):
        count = 0
        # Iterates through the grid and return the pos of the value
        for i in self.grid:
            for w in i:
                if w != val:
                    count +=1
                else:
                    return count

    def get_neighbors(self):
        # Gets the pos of the blank
        blank_index = self.get_index(None)
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

    def move_cell(self, val):
        # Return if the empty space is pressed
        if val is None:
            return
        blank_index = self.get_index(None)
        cell_index = val
        cell = self.get_value(val)
        # Gets the coordinate pos
        blank_row, blank_col = blank_index // 4, blank_index % 4
        cell_row, cell_col = cell_index // 4, cell_index % 4
        # Swaps the values
        self.grid[blank_row][blank_col], self.grid[cell_row][cell_col] = \
            self.grid[cell_row][cell_col], self.grid[blank_row][blank_col]

        if isinstance(cell, Cell):
            cell.change_pos(blank_index)
        self.moves += 1

    def get_value(self, val):
        count = 0
        for i in self.grid:
            for w in i:
                if val == count:
                    return w
                count += 1

    def handle_press(self, param):
        neighbors = self.get_neighbors()
        # Ensure we have valid neighbors
        if not neighbors:
            return None

        x_inc = 300 / 4
        y_inc = 350 / 4

        def get_coords(index):
            x, y = 0, 0
            if 0 <= index <= 3:
                x = index * x_inc
                y = 0
            elif 4 <= index <= 7:
                x = index * x_inc - 300
                y = y_inc
            elif 8 <= index <= 11:
                x = index * x_inc - 600
                y = y_inc * 2
            elif 12 <= index <= 15:
                x = index * x_inc - 900
                y = y_inc * 3
            return x, y

        click_x, click_y = param
        for neighbor in neighbors:
            x, y = get_coords(neighbor)
            if x <= click_x <= x + x_inc and y <= click_y <= y + y_inc:
                return neighbor

        return None

    def check_end(self):
        count = 1
        for row in self.grid:
            for cell in row:
                if cell == None or cell == "Blank":
                    if count == 16:  # Only the blank cell should be in this case
                        return True
                    continue
                if isinstance(cell, Cell) and cell.value != count:
                    return False
                count += 1
        return count == 16  # Ensure all 15 cells are in place and one blank cell

    def toArray(self):
        return [[e.value if isinstance(e, Cell) else None for e in i] for i in self.grid]
