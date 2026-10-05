import heapq

# Initial and Goal states
initial = (
    (2, 8, 3),
    (1, 6, 4),
    (7, 0, 5)
)

goal = (
    (1, 2, 3),
    (8, 0, 4),
    (7, 6, 5)
)


# Heuristic 1: Number of misplaced tiles
def misplaced_tiles(state):
    count = 0

    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1

    return count


# Heuristic 2: Manhattan Distance
def manhattan_distance(state):
    distance = 0

    for i in range(3):
        for j in range(3):
            tile = state[i][j]

            if tile != 0:
                # Find position of tile in goal state
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == tile:
                            distance += abs(i - x) + abs(j - y)

    return distance


# Generate possible moves
def get_neighbors(state):
    neighbors = []

    # Find blank position
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                blank_i = i
                blank_j = j

    # Possible movements: up, down, left, right
    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for di, dj in moves:
        new_i = blank_i + di
        new_j = blank_j + dj

        if 0 <= new_i < 3 and 0 <= new_j < 3:

            # Convert tuple to list
            new_state = [list(row) for row in state]

            # Swap blank with adjacent tile
            new_state[blank_i][blank_j], new_state[new_i][new_j] = \
                new_state[new_i][new_j], new_state[blank_i][blank_j]

            # Convert back to tuple
            new_state = tuple(tuple(row) for row in new_state)

            neighbors.append(new_state)

    return neighbors


# Print puzzle
def print_state(state):
    for row in state:
        print(row)
    print()


# A* Search
def a_star(initial, goal, heuristic):

    # Priority queue
    # (f, g, state, path)
    open_list = []

    g = 0
    h = heuristic(initial)
    f = g + h

    heapq.heappush(open_list, (f, g, initial, [initial]))

    # Store best cost for each state
    visited = {}

    while open_list:

        f, g, current, path = heapq.heappop(open_list)

        # If goal is reached
        if current == goal:
            return path

        # Avoid visiting a state with a higher cost
        if current in visited and visited[current] <= g:
            continue

        visited[current] = g

        # Generate next states
        for neighbor in get_neighbors(current):

            new_g = g + 1
            h = heuristic(neighbor)
            new_f = new_g + h

            new_path = path + [neighbor]

            heapq.heappush(
                open_list,
                (new_f, new_g, neighbor, new_path)
            )

    return None


# ---------------- MAIN PROGRAM ----------------

print("A* SEARCH - 8 PUZZLE")
print("---------------------")

print("\nInitial State:")
print_state(initial)

print("Goal State:")
print_state(goal)


# Case 1: Misplaced Tiles
print("CASE 1: MISPLACED TILES")
print("------------------------")

path = a_star(initial, goal, misplaced_tiles)

if path:
    print("Solution found!")
    print("Number of moves:", len(path) - 1)

    for i, state in enumerate(path):
        print("Step", i)
        print_state(state)
else:
    print("No solution found.")


# Case 2: Manhattan Distance
print("CASE 2: MANHATTAN DISTANCE")
print("---------------------------")

path = a_star(initial, goal, manhattan_distance)

if path:
    print("Solution found!")
    print("Number of moves:", len(path) - 1)

    for i, state in enumerate(path):
        print("Step", i)
        print_state(state)
else:
    print("No solution found.")



    