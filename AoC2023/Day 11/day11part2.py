import numpy as np
from itertools import combinations

def get_distance(x, y, row, col):
    dist = 0
    for i in range(y[0], x[0],1 if x[0] > y[0] else -1):
        dist += row[i]

    for i in range(y[1], x[1], 1 if x[1] > y[1] else -1):
        dist += col[i]

    return dist

def get_total_distance(lines, space):
    row_dict = {i:space for i in range(len(lines))}
    col_dict = {i:space for i in range(len(lines[0]))}
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                galaxies.append((i, j))
                row_dict[i] = 1
                col_dict[j] = 1
    return (get_distance(x, y, row_dict, col_dict) for x, y in combinations(galaxies, 2))

if __name__ == "__main__":
    filename = "input.txt"
    # filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()
        lines = np.array([list(x.strip('\n')) for x in lines])

    total_dist = sum(get_total_distance(lines, 1000000))

    print(total_dist)

#Part2: 702152204842
