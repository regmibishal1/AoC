import itertools
from collections import Counter


def check(currB, rest):
    dimList = [(0, 1), (1, 1), (2, 1), (0, -1), (1, -1), (2, -1)]
    maxLap = 12
    coord = []
    shiftList = []
    tempI = None
    tempJ = None
    for axis in range(3):
        k = [dim[axis] for dim in currB]

        for (tempK, fact) in dimList:
            if tempK == tempI or tempK == tempJ:
                continue

            dimD = [dim[tempK] * fact for dim in rest]
            disList = [b - a for (a, b) in itertools.product(k, dimD)]
            countOrd = Counter(disList).most_common(1)

            if countOrd[0][1] >= maxLap:
                break

        if countOrd[0][1] < maxLap:
            return None

        (tempJ, tempI) = (tempI, tempK)
        coord.append([val - countOrd[0][0] for val in dimD])
        shiftList.append(countOrd[0][0])

    return [list(zip(coord[0], coord[1], coord[2])), shiftList]


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [line.strip() for line in lines]
    data = list(filter(lambda x: x != '', data))
    scanners = []
    temp = []
    for i in data:
        if "---" in i:
            temp = []
            scanners.append(temp)
        else:
            temp.append(tuple(map(int, i.split(","))))

    beacons = set()
    curr = [scanners[0]]
    remain = scanners[1:]
    shifts = [(0, 0, 0)]
    while curr:
        currBeacon = curr.pop()
        temp = []
        for beacon in remain:
            update = check(currBeacon, beacon)
            if update:
                updated, shift = update
                shifts.append(shift)
                curr.append(updated)
            else:
                temp.append(beacon)
        remain = temp
        beacons.update(currBeacon)

    print("Beacons: " + str(len(beacons)))

    allCombination = itertools.product(shifts, shifts)
    distMax = 0
    for x, y in allCombination:
        tot = 0
        for (i, j) in zip(x, y):
            tot += abs(i - j)
        if tot > distMax:
            distMax = tot

    print("Max Distance: " + str(distMax))
