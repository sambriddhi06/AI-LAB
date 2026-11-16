import random
import math
N = 8
def calculate_cost(state):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j]:
                conflicts += 1
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts
def generate_neighbor(state):
    neighbor = state.copy()
    col = random.randint(0, N - 1)
    new_row = random.randint(0, N - 1)
    while new_row == neighbor[col]:
        new_row = random.randint(0, N - 1)
    neighbor[col] = new_row
    return neighbor
def display_board(state):
    print("\n  0 1 2 3 4 5 6 7")
    for row in range(N):
        print(row, end=" ")
        for col in range(N):
            if state[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
def simulated_annealing():
    restart = 0
    while True:
        restart += 1
        current = [random.randint(0, N - 1)
                   for _ in range(N)]
        current_cost = calculate_cost(current)
        T = 1000
        cooling_rate = 0.995
        print("\nRestart:", restart)
        print("Initial State:", current)
        print("Initial Cost:", current_cost)
        for step in range(20000):
            if current_cost == 0:
                print("\nSolution Found!")
                print("Steps:", step)
                print("Final State:", current)
                print("Final Cost:", current_cost)
                display_board(current)
                return current
            next_state = generate_neighbor(current)
            next_cost = calculate_cost(next_state)
            delta_E = current_cost - next_cost
            if delta_E > 0:
                current = next_state
                current_cost = next_cost
            else:
                probability = math.exp(delta_E / T)
                if random.random() < probability:
                    current = next_state
                    current_cost = next_cost
            T = T * cooling_rate
            if T < 0.01:
                break
print("SIMULATED ANNEALING - 8 QUEENS PROBLEM")
solution = simulated_annealing()
print("\nFinal Chessboard:")
display_board(solution)

print("Sambriddhi Prasai 1BF24CS268")