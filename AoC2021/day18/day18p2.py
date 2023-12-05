from copy import deepcopy
from math import floor, ceil


def checkSplit(currList):
    for x in range(len(currList)):
        if currList[x] not in ['[', ']'] and currList[x] >= 10:
            currList[x:x + 1] = ['[', floor(currList[x] / 2), ceil(currList[x] / 2), ']']
            return True, currList
    return False, currList


def checkExplode(currList):
    count = 0
    for x in range(len(currList)):
        if count == 4 and currList[x] == '[':
            lhs = currList[x + 1]
            rhs = currList[x + 2]
            for y in range(x - 1, 0, -1):
                if currList[y] not in ['[', ']']:
                    currList[y] += lhs
                    break
            for y in range(x + 4, len(currList)):
                if currList[y] not in ['[', ']']:
                    currList[y] += rhs
                    break
            return True, currList[:x] + [0] + currList[x + 4:]
        elif currList[x] == '[':
            count += 1
        elif currList[x] == ']':
            count -= 1
    return False, currList


def calcMag(currList, ind=0):
    if currList[ind] not in ['[', ']']:
        return currList[ind], ind
    lhs, ind = calcMag(currList, ind + 1)
    rhs, ind = calcMag(currList, ind + 1)
    return 3 * lhs + 2 * rhs, ind + 1


def reduceList(currList):
    reduced = True
    while reduced:
        reduced, currList = checkExplode(currList)
        if not reduced:
            reduced, currList = checkSplit(currList)

    return currList


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [line.strip() for line in lines]
    data = [list(map(lambda char: int(char) if char not in ['[', ']'] else char, line.replace(',', '')))
            for line in data]

    magMax = 0
    for i in data:
        for j in data:
            if i != j:
                curr = ['['] + deepcopy(i) + deepcopy(j) + [']']
                curr = reduceList(curr)
                mag = calcMag(curr)[0]
                if mag > magMax:
                    magMax = mag
    print(magMax)
