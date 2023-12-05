if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [line.strip('\n') for line in lines]
    count = [0] * len(data[0])
    for i in range(len(data[0])):
        ones = list(filter(lambda s: s[i] == "1", data))
        count[i] = len(ones)
    result = [1 if x >= len(data)//2 else 0 for x in count]
    result2 = [0 if x == 1 else 1 for x in result]
    print(''.join(str(x) for x in result))
    print(''.join(str(x) for x in result2))
