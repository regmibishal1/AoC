if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as f:
        lines = f.readlines()
    counter = 0
    for i in range(len(lines)-3):
        a = int(lines[i].strip('\n')) + int(lines[i+1].strip('\n')) + int(lines[i+2].strip('\n'))
        b = int(lines[i+1].strip('\n')) + int(lines[i+2].strip('\n')) + int(lines[i+3].strip('\n'))
        if a < b:
            counter += 1
    print(counter)