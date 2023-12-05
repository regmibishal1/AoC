import numpy as np

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [line.strip() for line in lines]
    instruction = [inst.split(' ')[2].split('=') for inst in data[data.index('') + 1:]]
    data = [[int(j) for j in i.split(',')] for i in data[:data.index('')]]

    x_max = 0
    for x in data:
        x_max = x[0] if x[0] > x_max else x_max

    y_max = 0
    for y in data:
        y_max = y[1] if y[1] > y_max else y_max

    # x is column y is rows
    row = [0] * (x_max + 1)
    page = [row.copy() for i in range(y_max + 1)]

    for i in data:
        page[i[1]][i[0]] = 1

    for i in instruction:
        if i[0] == 'y':
            counter = 1
            while counter + int(i[1]) <= y_max and int(i[1]) - counter >= 0:
                for x in range(x_max + 1):
                    page[int(i[1]) - counter][x] = page[int(i[1]) - counter][x] if page[int(i[1]) - counter][x] else \
                        page[int(i[1]) + counter][x]
                    page[int(i[1]) + counter][x] = 0
                counter += 1

        if i[0] == 'x':
            counter = 1
            while counter + int(i[1]) <= x_max and int(i[1]) - counter >= 0:
                for y in range(y_max + 1):
                    page[y][int(i[1]) - counter] = page[y][int(i[1]) - counter] if page[y][int(i[1]) - counter] else \
                        page[y][int(i[1]) + counter]
                    page[y][int(i[1]) + counter] = 0
                counter += 1

    for i in range(10):
        for j in range(50):
            print('#' if page[i][j] else ' ', end=" ")
        print()