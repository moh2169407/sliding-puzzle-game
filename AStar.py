import heapq
from heapq import heappush

from Node import Node

# Takes a node and goes backwards to the parent node
def reconstruct_path(current):
    path = []
    while current:
        path.append(current.move_pos)
        current = current.parent
    path.reverse()  # Reverse the path to show the solution from start to goal
    return path


class AStar:
    def __init__(self, grid):
        # The goals
        self.goal = [[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12],
                     [13,14,15,None]]
        self.grid = grid
        self.moves = 0

    def astar(self):
        # The open list, list containing node to be considered
        open_list = []
        # The closed list, list containing node that have already been looked at
        closed_list = set()  # Use a set for fast lookups
        # Using a heapq for value based queue
        heapq.heapify(open_list)
        # The starting node created from the starting board config
        starting_node = Node(self.grid, None, self.moves, 0)
        # Pushed on the heap
        heapq.heappush(open_list, starting_node)
        # Start
        while open_list:
            # The current node
            current = heapq.heappop(open_list)
            # if the current node is the end goal
            if current.grid == self.goal or current.h == 0:
                return current  # Found solution

            grid_tuple = tuple(map(tuple, current.grid))  # Convert grid to a hashable type
            # Prevents looking at node previously looked at
            if grid_tuple in closed_list:
                continue
            self.moves += 1
            # Adds it to the closed list
            closed_list.add(grid_tuple)
            # Generate the children, all the possible moves made at this current config
            for child in current.generate_children():
                child_tuple = tuple(map(tuple, child.grid))
                if child_tuple not in closed_list:
                    heapq.heappush(open_list, child)

        return None  # No solution found

