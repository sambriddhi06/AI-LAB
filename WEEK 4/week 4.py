import random
N = 4
def calculate_cost(state):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j]:
                conflicts += 1
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts
def display_board(state):
    for row in range(N):
        for col in range(N):
            if state[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()
    print()
def generate_neighbors(state):
    neighbors = []
    for col in range(N):
        for row in range(N):
            if state[col] != row:
                new_state = state.copy()
                new_state[col] = row
                neighbors.append(new_state)
    return neighbors
def hill_climbing():
    restart = 0
    while True:
        current = [random.randint(0, N - 1)
                   for _ in range(N)]
        restart += 1
        print("\n================================")
        print("Restart:", restart)
        print("Initial State:", current)
        print("Initial Cost:", calculate_cost(current))
        while True:
            current_cost = calculate_cost(current)
            print("\nCurrent State:", current)
            print("Current Cost:", current_cost)
            if current_cost == 0:
                print("\nGoal State Found!")
                display_board(current)
                print("Final Cost:", current_cost)
                return current
            neighbors = generate_neighbors(current)
            best_neighbor = current
            best_cost = current_cost
            print("\nNeighbor States and Costs:")
            for neighbor in neighbors:
                cost = calculate_cost(neighbor)
                print(neighbor, " Cost =", cost)
                if cost < best_cost:
                    best_cost = cost
                    best_neighbor = neighbor
            if best_cost >= current_cost:
                print("\nLocal Minimum Reached!")
                print("Restarting with a new state...")
                break
            current = best_neighbor
            print("\nMoving to Best Neighbor:", current)
            print("New Cost:", best_cost)
print("HILL CLIMBING ALGORITHM - 4 QUEENS")
solution = hill_climbing()
print("\nFinal Solution:", solution)
print("\nFinal Chessboard:")
display_board(solution)