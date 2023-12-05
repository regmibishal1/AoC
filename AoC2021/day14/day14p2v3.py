from collections import Counter

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [line.strip() for line in lines]
    start = data[0]
    elem = {pairs.split('->')[0].strip(): pairs.split('->')[1].strip() for pairs in data[2:]}

    # start off the list pairs counter
    counter = Counter()
    for ind in range(len(start)-1):
        counter[start[ind] + start[ind + 1]] += 1

    # keeping track of each pair created given the pairs we already have
    for i in range(40):
        tempCounter = Counter()
        for j in counter:
            tempCounter[j[0]+elem[j]] += counter[j]
            tempCounter[elem[j]+j[1]] += counter[j]
        counter = tempCounter

    # take the pair and turn it into singular char and count including the last char we ignored from the start
    finalCounter = Counter()
    for k in counter:
        finalCounter[k[0]] += counter[k]
    finalCounter[start[-1]] += 1

    # sorted by most common to least then take the first and last value to calculate
    sortedList = finalCounter.most_common()
    print(sortedList[0][1]-sortedList[-1][1])
