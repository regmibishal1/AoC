from collections import Counter

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [line.strip() for line in lines]
    start = data[0]
    elem = {tuple(pairs.split('->')[0].strip()): pairs.split('->')[1].strip() for pairs in data[2:]}

    for i in range(40):
        print(i)
        string = start
        pairs = list(zip(string[:len(start)-1], string[1:]))
        convertedPairs = list(map(elem.get, pairs))
        result = [None]*(len(list(string))+len(convertedPairs))
        result[::2] = list(string)
        result[1::2] = convertedPairs
        start = ''.join(result)
    counter = Counter(start)
    sortedList = counter.most_common()
    print(sortedList[0][1]-sortedList[-1][1])
