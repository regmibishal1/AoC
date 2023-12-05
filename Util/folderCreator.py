import os

for i in range(7, 26):
    pathToDir = '../Aoc2022'
    path = '{}/Day {}'.format(pathToDir, i)
    if not os.path.exists(path):
        os.mkdir(path)