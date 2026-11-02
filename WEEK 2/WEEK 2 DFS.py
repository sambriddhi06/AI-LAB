def dfs(state, goal, path, visited):
    if state == goal:
        return path

    visited.add(state)
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = []

    if row > 0:
        moves.append(zero - 3)
    if row < 2:
        moves.append(zero + 3)
    if col > 0:
        moves.append(zero - 1)
    if col < 2:
        moves.append(zero + 1)

    for move in moves:
        new_state = list(state)
        new_state[zero], new_state[move] = new_state[move], new_state[zero]
        new_state = tuple(new_state)

        if new_state not in visited:
            result = dfs(new_state, goal, path + [new_state], visited)

            if result:
                return result

    return None


def print_solution(solution):
    for state in solution:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()


initial = (1, 2, 3,
           0, 4, 6,
           7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution = dfs(initial, goal, [initial], set())

if solution:
    print("DFS Solution:")
    print_solution(solution)
else:
    print("No solution")

print ("Sambriddhi Prasai 1BF24C268")