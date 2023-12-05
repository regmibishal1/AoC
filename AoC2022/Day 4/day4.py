
def part1(lines):
    count = 0
    for i in lines:
        first, second = i.strip('\n').split(',')
        first = first.split('-')
        second = second.split('-')
        if (int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1])) or\
                (int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[1])):
            count += 1
    print(count)


def part2(lines):
    count = 0
    for i in lines:
        first, second = i.strip('\n').split(',')
        first = first.split('-')
        second = second.split('-')
        if not (int(first[1]) < int(second[0]) or int(first[0]) > int(second[1])):
            count += 1
    print(count)


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as f:
        lines = f.readlines()

    # part 1
    # part1(lines)
    part2(lines)