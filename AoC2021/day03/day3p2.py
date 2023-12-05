if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [line.strip('\n') for line in lines]
    data2 = data[:]
    for i in range(len(data[0])):
        ones = list(filter(lambda s: s[i] == "1", data))
        zeros = list(filter(lambda s: s[i] == "0", data))
        if len(ones) >= len(zeros):
            data = ones
        else:
            data = zeros

        if len(data) == 1:
            break

    print('Oxygen: ' + str(data))  # 509

    for i in range(len(data2[0])):
        ones = list(filter(lambda s: s[i] == "1", data2))
        zeros = list(filter(lambda s: s[i] == "0", data2))
        if len(ones) < len(zeros):
            data2 = ones
        else:
            data2 = zeros

        if len(data2) == 1:
            break

    print('CO2: ' + str(data2))  # 2693
