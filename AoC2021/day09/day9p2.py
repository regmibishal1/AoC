def search(arr, row, col, visited, count):
    rowNum = [-1, 0, 0, 1]
    colNum = [0, -1, 1, 0]
    visited[row][col] = True

    for k in range(4):
        if (row + rowNum[k] >= 0) and (row + rowNum[k] < len(arr)) and (col + colNum[k] >= 0) and (
                col + colNum[k] < len(arr[0])) and (
                arr[row + rowNum[k]][col + colNum[k]] != 9 and not visited[row + rowNum[k]][col + colNum[k]]):
            count[0] += 1
            search(arr, row + rowNum[k], col + colNum[k], visited, count)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [[int(num) for num in list(line.strip())] for line in lines]
    COL = len(data[0])
    ROW = len(data)
    visited = [[0] * COL for i in range(ROW)]
    sizes = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            test = True
            if i > 0 and data[i][j] >= data[i - 1][j]:
                test = False
            if i < len(data) - 1 and data[i][j] >= data[i + 1][j]:
                test = False
            if j > 0 and data[i][j] >= data[i][j - 1]:
                test = False
            if j < len(data[i]) - 1 and data[i][j] >= data[i][j + 1]:
                test = False
            if test and not visited[i][j]:
                count = [1]
                search(data, i, j, visited, count)
                sizes.append(count[0])
    sizes.sort(reverse=True)
    solution = sizes[0] * sizes[1] * sizes[2]
    print(solution)
