
start = (2, 8, 3,
         1, 6, 4,
         7, 0, 5)


goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)



def manhattan(state):

    distance = 0

    for i in range(9):

        if state[i] != 0:

            
            row = i // 3
            col = i % 3

            
            goal_index = goal.index(state[i])

            goal_row = goal_index // 3
            goal_col = goal_index % 3

            distance += abs(row - goal_row)
            distance += abs(col - goal_col)

    return distance



def get_neighbors(state):

    neighbors = []

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors



def print_state(state, g):

    h = manhattan(state)
    f = g + h

    print("g(n) =", g)
    print("h(n) =", h)
    print("f(n) =", f)

    for i in range(0, 9, 3):
        print(state[i:i+3])

    print()



def a_star():

    open_list = []

    g = 0
    h = manhattan(start)
    f = g + h

    open_list.append((f, g, start, [start]))

    visited = set()

    while open_list:

        
        best_index = 0

        for i in range(1, len(open_list)):
            if open_list[i][0] < open_list[best_index][0]:
                best_index = i

        
        f, g, state, path = open_list.pop(best_index)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:

            print("Solution found!")
            print("Total cost:", g)
            print()

            for depth, s in enumerate(path):
                print("State", depth)
                print_state(s, depth)

            return

        
        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                new_g = g + 1
                new_h = manhattan(neighbor)
                new_f = new_g + new_h

                open_list.append(
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    print("No solution found.")



a_star()