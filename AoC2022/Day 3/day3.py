if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as f:
        lines = f.readlines()

    priority = 0
    # for i in lines:
    for i in range(0, len(lines), 3):
        # val = i.strip('\n')
        # firstpart, secondpart = val[:len(val)//2], val[len(val)//2:]

        # firstpart = set([*firstpart])
        # secondpart = set([*secondpart])
        #
        # common = list(firstpart.intersection(secondpart))
        # priority += ord(common[0]) - 96 if common[0].islower() else ord(common[0]) - 64 + 26

        first = set([*(lines[i].strip('\n'))])
        second = set([*(lines[i+1].strip('\n'))])
        third = set([*(lines[i+2].strip('\n'))])

        common = list(first.intersection(second.intersection(third)))
        priority += ord(common[0]) - 96 if common[0].islower() else ord(common[0]) - 64 + 26

    print(priority)
