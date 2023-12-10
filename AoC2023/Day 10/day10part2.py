import numpy as np
import re

DIRECTION = {
    '|': [(1, 0), (-1, 0)],
    '-': [(0, 1), (0, -1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)],
}

def get_direction(curr_symbol, curr_pos, visited):
    for direction in DIRECTION[curr_symbol]:
        new_pos = [curr_pos[0] + direction[0], curr_pos[1] + direction[1]]
        if new_pos not in visited or grid[new_pos[0], new_pos[1]] == 'S':
            return new_pos

    raise Exception("No direction found")

if __name__ == "__main__":
    S = '7'
    filename = "input.txt"
    # filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()
        lines = [list(x.strip('\n')) for x in lines]

    grid = np.array(lines)

    # hard coding sadly
    start_i, start_j = np.where(grid == 'S')
    current = [start_i[0], start_j[0]]
    current_symbol = S
    visited = [current]
    while current_symbol != 'S':
        current = get_direction(current_symbol, current, visited)
        visited.append(current)
        current_symbol = grid[current[0], current[1]]

    # want to get rid of all the extra stuff
    new_grid = []
    for i in range(len(lines)):
        row = ""
        for j in range(len(lines[i])):
            if [i, j] not in visited:
                row += "."
            elif lines[i][j] == 'S':
                row += S
            else:
                row += lines[i][j]
        new_grid.append(row)


    # using symbols and how many times they occur to determine if in the middle or outside
    found = 0
    for row in new_grid:
        wall_count = 0
        row = re.sub(r"F-*J|L-*7", "|", row)
        row = re.sub(r"F-*7|L-*J|", "", row)
        for i in row:
            if i in "|":
                wall_count += 1
            if i == "." and wall_count % 2 == 1 :
                found += 1

    print(found)
