
if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [int(i) for i in lines[0].strip().split(',')]
    for i in range(80):
        counter = 0
        for j in range(len(data)):
            if data[j] == 0:
                counter += 1
                data[j] = 6
            else:
                data[j] -= 1
        data += ([8] * counter)
    print(len(data))



