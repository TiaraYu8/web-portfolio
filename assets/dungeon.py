import heapq

# Define the grid dimensions
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Define the grid with obstacles (1 denotes obstacles)
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Define the start and goal positions
start = (0, 0)
goal = (4, 4)

# Define possible moves (up, down, left, right)
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def heuristic(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def astar(grid, start, goal):
    open_list = [(0, start)]
    came_from = {}
    g_score = {pos: float('inf') for row in grid for pos in row}  # Initialize g_score for all grid cells
    g_score[start] = 0

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for move_x, move_y in moves:
            neighbor = (current[0] + move_x, current[1] + move_y)
            if 0 <= neighbor[0] < GRID_HEIGHT and 0 <= neighbor[1] < GRID_WIDTH and grid[neighbor[0]][neighbor[1]] != 1:
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score, neighbor))

    return None

def print_grid(grid, path=None):
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if path and (i, j) in path:
                print("P", end=" ")
            elif grid[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

path = astar(grid, start, goal)
if path:
    print("Path found:")
    print_grid(grid, path)
else:
    print("Path not found.")
