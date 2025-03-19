# Sliding 15-Puzzle Game

## Date: March 16, 2025

## Description
This project is a recreation of the classic 15-puzzle game, also known as the sliding tile puzzle. The goal of the game is to arrange the numbered tiles in the correct order by sliding them into the empty space. The game is solved using the A* search algorithm with different heuristic functions to determine the optimal path to the solution.

## Features
- Implements A* search algorithm to find the shortest solution path.
- Supports multiple heuristic functions (e.g., Manhattan distance, misplaced tiles).
- Generates solvable board configurations.
- Tracks visited nodes and performance metrics.

## Installation & Usage
### Prerequisites
- Python 3.x

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/sliding-16-puzzle.git
cd sliding-16-puzzle


### Running the Project
```bash
python main.py
```

## How It Works
### Algorithm
The solver utilizes the A* search algorithm, which evaluates possible moves based on:
1. **g(n)**: The cost to reach the current state.
2. **h(n)**: The estimated cost to reach the goal (heuristic function).
3. **f(n) = g(n) + h(n)**: The total estimated cost.

### Board Generation Issue & Solution
Initially, I attempted to generate random board configurations, but I later discovered that not all randomly shuffled boards are solvable. This was a major issue since the algorithm could not find solutions for certain inputs. To resolve this, I implemented a method that starts with a solved board and performs valid moves in reverse to ensure solvability.

## Problems Encountered & Lessons Learned
- **Random board generation issue**: Learned about puzzle solvability constraints and how to properly generate solvable configurations.
- **Lack of documentation**: Initially, I had minimal comments and documentation, making it hard to return to the project after a long break. This experience reinforced the importance of writing clear documentation.
- **Debugging heuristic function**: I noticed that the heuristic values were not decreasing as expected. Debugging this issue taught me to validate each step and ensure that heuristic calculations are applied correctly to newly generated states.

## Results & Performance
- The solver successfully completes puzzles in a reasonable time for most cases.
- Future improvements include optimizing the heuristic function and implementing a GUI visualization.

## Future Improvements
- I want the size of the puzzle to change dynamically
- The cost function for the a star doesn't work and resutls in a inf loop, I got it to work without it but it resembles closer to a greedy algorithm 

## Technologies Used
- **Programming Language**: Python
- **Libraries**: NumPy, PriorityQueue

## Video
https://github.com/user-attachments/assets/eac68258-1198-47ea-b3b5-71b55f18f24b


