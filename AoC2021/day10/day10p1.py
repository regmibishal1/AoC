open_list = ["[", "{", "(", "<"]
close_list = ["]", "}", ")", ">"]

stringDict = {"]": 57, "}": 1197, ")": 3, ">": 25137}


def check(string):
    stack = []
    for j in string:
        if j in open_list:
            stack.append(j)
        elif j in close_list:
            ind = close_list.index(j)
            if (len(stack) > 0) and (open_list[ind] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return stringDict[j]
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [line.strip() for line in lines]
    tot = 0
    for i in data:
        tot += check(i)

    print(tot)
