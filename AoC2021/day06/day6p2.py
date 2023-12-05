from collections import Counter

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [int(i) for i in lines[0].strip().split(',')]
    dataDict = dict(Counter(data))
    dataDict.update({0: 0, 6: 0, 7: 0, 8: 0})
    for i in range(256):
        temp = dataDict[0]
        for j in range(8):
            dataDict[j] = dataDict[j + 1]
        dataDict[8] = temp
        dataDict[6] += temp
    print(sum(dataDict.values()))
