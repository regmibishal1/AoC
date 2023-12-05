if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as f:
        lines = f.readlines()

    maxCal = 0
    tempMax = 0
    for i in lines:
        if i != "\n":
            tempMax += float(i.strip('\n'))
        else:
            maxCal = max(maxCal, tempMax)
            tempMax = 0
    print(maxCal)