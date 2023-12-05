if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as f:
        lines = f.readlines()

    maxCal = []
    tempMax = 0
    for i in lines:
        if i != "\n":
            tempMax += float(i.strip('\n'))
        else:
            maxCal.append(tempMax)
            tempMax = 0
    print(sum(sorted(maxCal, reverse=True)[:3]))
