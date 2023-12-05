def getNum(strings, string):
    for x in strings:
        if len(strings[x]) == len(string):
            if checkMissing(list(strings[x]), list(string)) == 0:
                return str(x)


def checkMissing(list1, list2):
    return len(set(list1) - set(list2))


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [[comb.strip().split() for comb in line.strip('\n').split('|')] for line in lines]
    total = 0
    for i in data:
        # split up the list to the different parts
        lenSix = list(filter(lambda x: len(x) == 6, i[0]))
        lenFive = list(filter(lambda x: len(x) == 5, i[0]))
        lenOther = list(filter(lambda x: len(x) != 5 and len(x) != 6, i[0]))

        # working with one
        one = list(filter(lambda x: len(x) == 2, lenOther))
        if not one:
            print('Error Missing one')
            exit(-1)

        one = one[0]

        seven = list(filter(lambda x: len(x) == 3, lenOther))
        if not seven:
            print('Error Missing seven')
            exit(-1)
        seven = seven[0]

        four = list(filter(lambda x: len(x) == 4, lenOther))
        if not four:
            print('Error Missing four')
            exit(-1)
        four = four[0]

        eight = list(filter(lambda x: len(x) == 7, lenOther))
        if not eight:
            print('Error Missing eight')
            exit(-1)
        eight = eight[0]

        six = list(filter(lambda x: checkMissing(list(x), list(one)) == 5, lenSix))
        if not six:
            print('Error Missing six')
            exit(-1)
        six = six[0]

        lenSix = list(filter(lambda x: x != six, lenSix))

        zero = list(filter(lambda x: checkMissing(list(x), list(set(four) - set(one))) == 5, lenSix))
        if not zero:
            print('Error Missing zero')
            exit(-1)
        zero = zero[0]

        nine = list(filter(lambda x: x != zero, lenSix))
        if not nine:
            print('Error Missing nine')
            exit(-1)
        nine = nine[0]

        five = list(filter(lambda x: checkMissing(list(six), list(x)) == 1, lenFive))
        if not five:
            print('Error Missing nine')
            exit(-1)
        five = five[0]

        lenFive = list(filter(lambda x: x != five, lenFive))

        two = list(filter(lambda x: checkMissing(list(five), list(x)) == 2, lenFive))
        if not two:
            print('Error Missing two')
            exit(-1)
        two = two[0]

        three = list(filter(lambda x: x != two, lenFive))
        if not three:
            print('Error Missing three')
            exit(-1)
        three = three[0]

        numDict = {0: zero, 2: two, 3: three, 5: five, 6: six, 9: nine}

        num = ''
        for j in i[1]:
            match len(j):
                case 2:
                    num += '1'
                case 3:
                    num += '7'
                case 4:
                    num += '4'
                case 7:
                    num += '8'
                case 5:
                    num += getNum(numDict, j)
                case 6:
                    num += getNum(numDict, j)

        # print(int(num))
        total += int(num)

    print(total)

