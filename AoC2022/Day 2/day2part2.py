if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as f:
        lines = f.readlines()

    WIN = {"A": "Y", "B": "Z", "C": "X"}
    LOSS = {"A": "Z", "B": "X", "C": "Y"}
    DRAW = {"A": "X", "B": "Y", "C": "Z"}
    mapPoint = {"X": 1, "Y": 2, "Z": 3}

    points = 0

    for i in lines:
        val = i.strip('\n')
        if val.split()[1] == "X":
            points += mapPoint[LOSS[val.split()[0]]]

        elif val.split()[1] == "Y":
            points += mapPoint[DRAW[val.split()[0]]] + 3

        elif val.split()[1] == "Z":
            points += mapPoint[WIN[val.split()[0]]] + 6
    print(points)
