import numpy as np

def pPrint(grid):
    for row in grid:
        print(row)

def updateRow(cord, grid):
    for i in range(cord[0][1], (cord[1][1] + 1)):
        grid[i][cord[0][0]] += 1
    for i in range(cord[1][1], (cord[0][1] + 1)):
        grid[i][cord[0][0]] += 1
    # pPrint(grid)


def updateCol(cord, grid):
    for i in range(cord[0][0], cord[1][0] + 1):
        grid[cord[0][1]][i] += 1
    for i in range(cord[1][0], cord[0][0] + 1):
        grid[cord[0][1]][i] += 1
    # pPrint(grid)

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [line.strip('\n') for line in lines]
    res = [[[ int(val) for val in cord.strip().split(',')] for cord in val.split('->')] for val in data]
    board = [[0 for point in range(1000)] for val in range(1000)]

    for cords in res:
        # print(cords)
        if cords[0][0] == cords[1][0]:
            updateRow(cords, board)
        elif cords[0][1] == cords[1][1]:
            updateCol(cords, board)

    numArray = np.asarray(board)
    print((numArray >= 2).sum())

