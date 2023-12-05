if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [[int(num) for num in list(line.strip())] for line in lines]
    sum = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            test = True
            if i > 0 and data[i][j] >= data[i-1][j]:
                test = False
            if i < len(data) - 1 and data[i][j] >= data[i+1][j]:
                test = False
            if j > 0 and data[i][j] >= data[i][j-1]:
                test = False
            if j < len(data[i]) - 1 and data[i][j] >= data[i][j+1]:
                test = False
            if test:
                print(j, i, data[i][j])
                sum += data[i][j] + 1
    print(sum)

