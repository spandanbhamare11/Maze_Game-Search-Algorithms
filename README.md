# Maze_Game-Search-Algorithms
GUI-based AI Maze Solver implementing BFS (Uninformed), A* (Informed), and Adversarial Search using Python and Pygame.

# Maze AI: Search Algorithms Visualization

This project is a GUI-based simulation that demonstrates fundamental Artificial Intelligence search techniques using a maze environment. The system showcases how different search strategies work in a dynamic and adversarial setting.

# Features

- GUI visualization using Pygame
- Uninformed Search: Breadth First Search (BFS)
- Informed Search: A* Algorithm
- Adversarial Environment (Enemy chasing the player)
- Dynamic path recalculation
- Randomized enemy behavior (different outcome each run)
- Keyboard-based algorithm selection

---

# Algorithms Implemented

 1. Breadth First Search (BFS)
- Uninformed search technique
- Explores nodes level by level
- Guarantees shortest path
- Higher memory usage

 2. A* Search
- Informed search algorithm
- Uses heuristic: Manhattan Distance
- Faster and more efficient than BFS

Formula: f(n) = g(n) + h(n)


Where:
- g(n) = cost from start
- h(n) = estimated distance to goal

### 3. Adversarial Behavior
- Enemy acts as an opponent
- Moves toward the player strategically
- 70% optimal moves
- 30% random moves to simulate uncertainty

---

## Technologies Used

- Python 3
- Pygame
- Heapq (Priority Queue)
- Math
- Random

---

## How It Works

1. User runs the program
2. Press:
   - `1` → BFS
   - `2` → A*
3. Player automatically navigates toward the goal
4. Enemy moves adversarially to catch the player
5. Simulation ends when:
   - Player reaches the goal, or
   - Enemy catches the player

Each run may produce different results due to randomized enemy behavior.

---

# Controls

| Key | Action |
|-----|--------|
| 1   | Run BFS (Uninformed Search) |
| 2   | Run A* (Informed Search) |
| Close window | Exit |

---

# Color Legend

| Color | Meaning |
|-------|---------|
| Blue  | Player |
| Red   | Enemy |
| Green | Goal |
| Black | Obstacle |
| White | Free path |

---


---

## Applications

- Game AI
- Robot navigation
- Path planning systems
- Autonomous agents
- AI learning and visualization

---

# Future Improvements

- Alpha-Beta pruning
- Multiple enemies
- Larger maze
- Difficulty levels
- User-controlled player
- Web-based version

---

# Author

**Spandan Bhamare**  
Computer Science Engineering Student

---

# License

This project is created for educational purposes.

