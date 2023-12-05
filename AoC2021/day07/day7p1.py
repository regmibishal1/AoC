if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [int(i) for i in lines[0].strip().split(',')]
    data.sort()
    center = data[len(data) // 2]
    sumVal = sum([abs(center - data[i]) for i in range(len(data))])
    print(sumVal)
