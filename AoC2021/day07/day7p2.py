import math
import statistics

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [int(i) for i in lines[0].strip().split(',')]
    center = math.ceil(statistics.mean(data))
    lowerCenter = math.trunc(statistics.mean(data))
    sumVal = sum([(abs(center - data[i])*(abs(center - data[i]) + 1))/2 for i in range(len(data))])
    lowerSumVal = sum([(abs(lowerCenter - data[i])*(abs(lowerCenter - data[i]) + 1))/2 for i in range(len(data))])
    print(center, lowerCenter)
    print(int(sumVal), int(lowerSumVal))




