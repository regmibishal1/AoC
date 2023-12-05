from itertools import groupby
import copy


def addUp(board):
    board = [[int(x) if x != 'X' else 0 for x in row] for row in board]
    return sum(list(map(sum, board)))


def wonCheck(board):
    checkRow = ['X', 'X', 'X', 'X', 'X']
    if checkRow in board or checkRow in list(map(list, zip(*board))):
        return True
    return False


def lossCheck(board):
    return not wonCheck(board)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    nums = lines[0].strip('\n').split(',')
    data = [line.strip('\n') for line in lines[1:]]
    tables = [list(sub) for ele, sub in groupby(data, key=bool) if ele]
    tables = [[row.replace("  ", " ").strip().split(' ') for row in table] for table in tables]
    tot = 0
    for i in nums:
        tables = [[[x if i != x else 'X' for x in row] for row in table] for table in tables]
        won = list(filter(wonCheck, tables))
        notWon = list(filter(lossCheck, tables))
        if len(notWon) == 0 and len(won) == 1:
            tot = addUp(won[0])
            tot *= int(i)
            break
        else:
            tables = copy.deepcopy(notWon)
    print(tot)
