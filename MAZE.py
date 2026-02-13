import pygame
import heapq
import math
import sys
import random

# -----------------------------
# Settings
# -----------------------------
ROWS, COLS = 6, 6
CELL_SIZE = 90
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE + 80

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (50,100,255)
RED = (220,50,50)
GREEN = (50,200,50)
GRAY = (200,200,200)
YELLOW = (255,220,0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze AI Project")
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

# -----------------------------
# Maze Layout
# -----------------------------
maze = [
    [0,0,0,0,1,0],
    [1,1,0,0,1,0],
    [0,0,0,1,0,0],
    [0,1,0,0,0,1],
    [0,1,0,1,0,0],
    [0,0,0,0,0,0]
]

player_start = (0,0)
enemy_start = (5,0)
goal = (5,5)

# -----------------------------
# Helper Functions
# -----------------------------
def valid_moves(pos):
    x,y = pos
    moves = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    result = []
    for nx,ny in moves:
        if 0<=nx<ROWS and 0<=ny<COLS and maze[nx][ny]==0:
            result.append((nx,ny))
    return result

def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# -----------------------------
# BFS (Uninformed)
# -----------------------------
def bfs(start, goal):
    queue = [start]
    visited = {start: None}

    while queue:
        current = queue.pop(0)
        if current == goal:
            break

        for move in valid_moves(current):
            if move not in visited:
                visited[move] = current
                queue.append(move)

    path = []
    node = goal
    while node:
        path.append(node)
        node = visited.get(node)
    path.reverse()
    return path

# -----------------------------
# A* (Informed)
# -----------------------------
def astar(start, goal):
    open_list = []
    heapq.heappush(open_list,(0,start))
    came = {}
    g = {start:0}

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            break

        for n in valid_moves(current):
            temp_g = g[current] + 1
            if n not in g or temp_g < g[n]:
                g[n] = temp_g
                f = temp_g + heuristic(n, goal)
                heapq.heappush(open_list,(f,n))
                came[n] = current

    path = []
    node = goal
    while node in came:
        path.append(node)
        node = came[node]
    path.append(start)
    path.reverse()
    return path

# -----------------------------
# Enemy Movement (Adversarial + Random)
# 70% smart, 30% random
# -----------------------------
def enemy_move(enemy, player):
    moves = valid_moves(enemy)
    if not moves:
        return enemy

    # Smart move (minimize distance)
    if random.random() < 0.7:
        best_move = enemy
        best_val = math.inf

        for move in moves:
            dist = heuristic(move, player)
            if dist < best_val:
                best_val = dist
                best_move = move

        return best_move

    # Random move
    return random.choice(moves)

# -----------------------------
# Drawing Functions
# -----------------------------
def draw_grid(player, enemy):
    screen.fill(WHITE)

    for i in range(ROWS):
        for j in range(COLS):
            rect = pygame.Rect(j*CELL_SIZE, i*CELL_SIZE+80, CELL_SIZE, CELL_SIZE)

            if maze[i][j] == 1:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, GRAY, rect, 1)

            if (i,j) == goal:
                pygame.draw.rect(screen, GREEN, rect)

            if (i,j) == player:
                pygame.draw.rect(screen, BLUE, rect)

            if (i,j) == enemy:
                pygame.draw.rect(screen, RED, rect)

def draw_menu():
    pygame.draw.rect(screen, YELLOW, (0,0,WIDTH,80))
    text = font.render("Press 1: BFS    Press 2: A*", True, BLACK)
    screen.blit(text, (WIDTH//4, 30))

# -----------------------------
# Game Simulation (Dynamic Player)
# -----------------------------
def run_game(search_type):
    player = player_start
    enemy = enemy_start
    running = True

    print(f"Running {search_type.upper()}")

    while running:
        clock.tick(2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Recalculate path every step (dynamic AI)
        if search_type == "bfs":
            path = bfs(player, goal)
        else:
            path = astar(player, goal)

        # Move player one step along path
        if len(path) > 1:
            player = path[1]

        # Enemy moves (smart + random)
        enemy = enemy_move(enemy, player)

        draw_menu()
        draw_grid(player, enemy)
        pygame.display.update()

        # Check conditions
        if player == enemy:
            print("Enemy caught player!")
            pygame.time.delay(1000)
            return

        if player == goal:
            print("Player reached goal!")
            pygame.time.delay(1000)
            return

# -----------------------------
# Main Loop
# -----------------------------
def main():
    while True:
        screen.fill(WHITE)
        draw_menu()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    run_game("bfs")
                if event.key == pygame.K_2:
                    run_game("astar")

main()
