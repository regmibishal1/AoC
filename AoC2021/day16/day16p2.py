from functools import reduce
from operator import mul

hexDictionary = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}


def multiply(val):
    return reduce(mul, val)


def checkString(biStr):
    version, ptype, content = biStr[0:3], biStr[3:6], biStr[6:]

    if int(ptype, 2) == 4:
        nextInd = 0
        binaryBits = ""
        for ind in range(0, len(content), 5):
            binaryBits += content[ind + 1:ind + 5]
            if content[ind] == '0':
                nextInd = ind
                break
        value = int(binaryBits, 2)
        return value, biStr[nextInd + 11:]

    else:
        if content[0] == '0':
            length = int(content[1:16], 2)
            subpacketBinary = content[16:16 + length]
            rest = content[16 + length:]
            subpackets = []
            while subpacketBinary:
                subpackets.append('')
                subpackets[-1], subpacketBinary = checkString(subpacketBinary)

        if content[0] == '1':
            cnt = int(content[1:12], 2)
            subpacketBinary = content[12:]
            subpackets = []
            for _ in range(cnt):
                subpackets.append('')
                subpackets[-1], subpacketBinary = checkString(subpacketBinary)
            rest = subpacketBinary

        match int(ptype, 2):
            case 0:
                subpackets = sum(subpackets)

            case 1:
                subpackets = multiply(subpackets)

            case 2:
                subpackets = min(subpackets)

            case 3:
                subpackets = max(subpackets)

            case 4:
                subpackets = 1 if subpackets[0] > subpackets[1] else 0

            case 5:
                subpackets = 1 if subpackets[0] < subpackets[1] else 0

            case 6:
                subpackets = 1 if subpackets[0] == subpackets[1] else 0

        return subpackets, rest


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [line.strip() for line in lines]
    binary = ''.join(list(map(lambda x: hexDictionary[x], list(data[0]))))
    sol = checkString(binary)
    print(sol)
