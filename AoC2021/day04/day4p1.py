from itertools import groupby


def addUp(board):
    board = [[int(x) if x != 'X' else 0 for x in row] for row in board]
    return sum(list(map(sum, board)))


def check(board):
    checkRow = ['X', 'X', 'X', 'X', 'X']
    if checkRow in board or checkRow in list(map(list, zip(*board))):
        return True
    return False


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    nums = lines[0].strip('\n').split(',')
    data = [line.strip('\n') for line in lines[1:]]
    tables = [list(sub) for ele, sub in groupby(data, key=bool) if ele]
    tables = [[row.replace("  ", " ").strip().split(' ') for row in table] for table in tables]
    bool = False
    tot = 0

    for i in nums:
        if bool:
            break
        tables = [[[x if i != x else 'X' for x in row] for row in table] for table in tables]
        for j in range(len(tables)):
            if check(tables[j]):
                tot = addUp(tables[j])
                tot *= int(i)
                bool = True
                break
    print(tot)
