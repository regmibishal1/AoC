import heapq


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [[int(point) for point in list(line.strip())] for line in lines]
    m, n = (len(data), len(data[0]))
    costArr = {}
    visited = set()

    tempQueue = [(0, 0, 0)]
    heapq.heapify(tempQueue)

    delta = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    while len(tempQueue) > 0:
        cost, row, col = heapq.heappop(tempQueue)

        if (row, col) in visited:
            continue
        visited.add((row, col))

        costArr[(row, col)] = cost

        if row == m - 1 and col == n - 1:
            print(costArr[(m - 1, n - 1)])
            break

        for deltaRow, deltaCol in delta:
            newRow = row + deltaRow
            newCol = col + deltaCol
            if not (0 <= newRow < m and 0 <= newCol < n):
                continue
            else:
                heapq.heappush(tempQueue, (data[newRow][newCol] + cost, newRow, newCol))
