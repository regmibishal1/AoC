
def isSymbol(char):
    return char != "." and not char.isdigit()

def debugPrint(i, j, num):
    print(num, lines[max(i-1, 0)][max(j-1, 0)], lines[max(i-1, 0)][j], lines[max(i-1, 0)][min(j+1, n-1)], lines[i][max(j-1, 0)],
          lines[i][min(j+1, n-1)], lines[min(i+1, m-1)][max(j-1, 0)], lines[min(i+1, m-1)][j], lines[min(i+1, m-1)][min(j+1, n-1)])


if __name__ == "__main__":
    filename = "input.txt"
    # filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()

    numbers = []
    m = len(lines)
    for i in range(m):
        lines[i] = lines[i].strip()
        number = ""
        n = len(lines[i])
        valid = False
        index = ()
        for j in range(n):
            if lines[i][j].isdigit():
                number += lines[i][j]

                # checking adjacent values to see if they are symbols
                if (isSymbol(lines[max(i-1, 0)][max(j-1, 0)]) or
                    isSymbol(lines[max(i-1, 0)][j]) or
                    isSymbol(lines[max(i-1, 0)][min(j+1, n-1)]) or
                    isSymbol(lines[i][max(j-1, 0)]) or
                    isSymbol(lines[i][min(j+1, n-1)]) or
                    isSymbol(lines[min(i+1, m-1)][max(j-1, 0)]) or
                    isSymbol(lines[min(i+1, m-1)][j]) or
                    isSymbol(lines[min(i+1, m-1)][min(j+1, n-1)])):
                    valid = True
                    # index = (i, j)
            elif number != "":
                if valid:
                    # debugPrint(index[0], index[1], number)
                    numbers.append(int(number))
                number = ""
                valid = False
            else:
                valid = False
                number = ""

        # handling end of line cases
        if number != "" and valid:
            numbers.append(int(number))
    print(sum(numbers))




