def dls(state, goal, depth, path, count):

    count[0] += 1

    if state == goal:
        return path

    if depth == 0:
        return None

    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = []

    if col < 2:
        moves.append(zero + 1)   # Right
    if row < 2:
        moves.append(zero + 3)   # Down
    if row > 0:
        moves.append(zero - 3)   # Up
    if col > 0:
        moves.append(zero - 1)   # Left

    for move in moves:

        new_state = list(state)
        new_state[zero], new_state[move] = \
            new_state[move], new_state[zero]

        new_state = tuple(new_state)

        if new_state not in path:

            result = dls(
                new_state,
                goal,
                depth - 1,
                path + [new_state],
                count
            )

            if result:
                return result

    return None


def ids(initial, goal):

    depth = 0
    count = [0]

    while True:

        solution = dls(
            initial,
            goal,
            depth,
            [initial],
            count
        )

        if solution:
            return solution, count[0], depth

        depth += 1


def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])


initial = (
    1, 2, 3,
    0, 4, 6,
    7, 5, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

solution, count, depth = ids(initial, goal)

print("INITIAL STATE:")
print_state(initial)

print("\nFINAL STATE:")
print_state(goal)

print("\nSOLUTION:")
for state in solution:
    print_state(state)
    print()

print("Depth at which goal was found:", depth)
print("Total Number of States Explored:", count)

print("Sambriddhi Prasai")