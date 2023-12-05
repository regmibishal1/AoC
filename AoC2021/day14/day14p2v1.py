from collections import Counter

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [line.strip() for line in lines]
    start = data[0]
    elem = {pairs.split('->')[0].strip(): pairs.split('->')[1].strip() for pairs in data[2:]}

    for i in range(40):
        print(i)
        string = start
        new = ''.join([string[j] + elem[string[j] + string[j+1]] for j in range(len(string) - 1)])
        new += string[-1]
        start = new
    counter = Counter(new)
    sortedList = counter.most_common()
    print(sortedList[0][1]-sortedList[-1][1])
