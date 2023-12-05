import numpy as np


def search(arr, row, col, visited):
    rowNum = [-1, -1, -1, 0, 0, 1, 1, 1]
    colNum = [-1, 0, 1, -1, 1, -1, 0, 1]

    visited[row][col] = 1

    for k in range(8):
        if (row + rowNum[k] >= 0) and (row + rowNum[k] < len(arr)) and (col + colNum[k] >= 0) and (
                col + colNum[k] < len(arr[0])):
            if arr[row + rowNum[k]][col + colNum[k]] + 1 == 10:
                visited[row + rowNum[k]][col + colNum[k]] = 0
            arr[row + rowNum[k]][col + colNum[k]] += 1


def check(arr):
    columns = len(arr[0])
    rows = len(arr)
    visitMat = np.array([[0] * columns for _ in range(rows)])

    finished = False
    while not finished:
        for x in range(rows):
            for y in range(columns):
                if arr[x][y] > 9 and not visitMat[x][y]:
                    search(data, x, y, visitMat)
                else:
                    visitMat[x][y] = 1
        finished = False if (visitMat == 0).sum() > 0 and (arr > 9).sum() > 0 else True
    arr[arr > 9] = 0
    return (arr == 0).sum()


if __name__ == "__main__":
    with open("test.txt") as f:
        lines = f.readlines()
    data = np.array([[int(num) for num in list(line.strip())] for line in lines])

    total = 0
    print(data)
    for i in range(100):
        data = data + 1
        total += check(data)
        print(data)

    print(total)
