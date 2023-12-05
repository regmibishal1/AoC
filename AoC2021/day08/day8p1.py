if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [[comb.strip().split() for comb in line.strip('\n').split('|')] for line in lines]
    count = 0
    for i in data:
        for j in i[1]:
            if len(j) in [2, 3, 4, 7]:
                count += 1
    print(count)
