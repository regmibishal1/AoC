if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as f:
        lines = f.readlines()
    depth = 0
    horizontal = 0
    aim = 0
    for i in lines:
        match i.split()[0]:
            case 'forward':
                horizontal += int(i.split()[1])
                depth += aim * int(i.split()[1])
            case 'down':
                aim += int(i.split()[1])
            case  'up':
                aim -= int(i.split()[1])

    print(depth, horizontal, depth * horizontal)
