open_list = ["[", "{", "(", "<"]
close_list = ["]", "}", ")", ">"]

stringDict = {"]": 2, "}": 3, ")": 1, ">": 4}


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
                return ''
    return stack


def getScore(chain):
    tot = 0
    for i in chain:
        tot *= 5
        tot += stringDict[i]

    return tot


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
    data = [line.strip() for line in lines]

    unCorrupted = []
    for x in data:
        unCorrupted.append(check(x))
    missing = [''.join([close_list[open_list.index(y)] for y in x[::-1]]) for x in list(filter(lambda s: s != '', unCorrupted))]

    scores = []
    for x in missing:
        scores.append(getScore(x))

    scores.sort()
    print(scores[len(scores) // 2])  # index starting at zero allows us to use the truncated value
