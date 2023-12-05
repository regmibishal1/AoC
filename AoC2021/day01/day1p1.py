if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as f:
        lines = f.readlines()
    counter = 0
    for i in range(len(lines)-1):
        if int(lines[i].strip('\n')) < int(lines[i + 1].strip('\n')):
            counter += 1
    print(counter)
