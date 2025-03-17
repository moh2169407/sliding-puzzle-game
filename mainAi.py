import time
from Node import Node
from Cells import *
from AStar import AI


# Constants:
# Keeps track of the run time
starting_time = time.time()
pg.init()
# Creates a screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Game")
running = True
win = False
clock = pg.time.Clock()
# Cells for the game
cells = Cells()
ai = AI(cells)
solution = ai.astar()
# Game Loop
while running:
    cells.draw(screen)
    # Checks for events
    for events in pg.event.get():
        if win:
            keys = pg.key.get_pressed()
            if keys[pg.K_ESCAPE]:
                running = False
            else: continue
        # if the close button is pressed, quit
        if events.type == pg.QUIT:
            running = False
        if cells.check_end():
            screen.fill(BLACK)
            end_time = time.time()
            font = pg.font.Font(None, 50)
            text = font.render("Game Over", True, WHITE)
            text_rect = text.get_rect()
            text_rect.center = (WIDTH / 2, HEIGHT / 2)
            screen.blit(text, text_rect)
            print("Game Over")
            print("Time: " + str(end_time - starting_time))
            print(f'Moves: {cells.moves}')
            win = True
        # Updates the screen
        pg.display.flip()
        # 60 FPS
        clock.tick(60)
pg.quit()