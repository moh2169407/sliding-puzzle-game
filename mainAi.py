import time

from AStar import AStar, reconstruct_path
from Cells import *
# Constants:
# Keeps track of the run time
starting_time = time.time()
pg.init()
# Creates a screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Game")
running = True
clock = pg.time.Clock()
runtime = 0
# Cells for the game
cells = Cells()
astar = AStar(cells.toArray())
# The node with the solution
solution = astar.astar()
# The path to the solved puzzle
path = reconstruct_path(solution)
# The game bool
finished = False
# Game Loop
index = 0
while running:
    cells.draw(screen)
    # Checks for events
    for events in pg.event.get():
        # if the close button is pressed, quit
        if events.type == pg.QUIT:
            running = False
    pg.display.flip()
    # 60 FPS
    clock.tick(60)
    if index <= len(path) - 1:
        cells.move_cell(path[index])
        index += 1
    else:
        running = False
        finished = True
    if not finished:
        runtime = time.time() - starting_time
# Print the stats on the terminal
print("Game Over")
print(f'{runtime} seconds')
print(f'Moves:{astar.moves}')
# Game Over, display the solved board
while finished:
    for events in pg.event.get():
        # if the close button is pressed, quit
        if events.type == pg.QUIT:
            finished = False
    pg.display.flip()

pg.quit()