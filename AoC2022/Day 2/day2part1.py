if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as f:
        lines = f.readlines()

    WINS = ["A Y", "B Z", "C X"]
    LOSS = ["A Z", "B X", "C Y"]
    DRAW = ["A X", "B Y", "C Z"]
    mapPoint = {"X": 1, "Y": 2, "Z": 3}

    points = 0

    for i in lines:
        val = i.strip('\n')
        pick = mapPoint[val.split()[1]]

        if val in WINS:
            points += (pick + 6)
        elif val in DRAW:
            points += (pick + 3)
        else:
            points += pick

    print(points)
