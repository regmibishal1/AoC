
def iterate(pixel, bit):
    mini = min(pixs[0] for pixs in pixel)
    maxi = max(pixs[0] for pixs in pixel)
    minj = min(pixs[1] for pixs in pixel)
    maxj = max(pixs[1] for pixs in pixel)

    enhanced = set()
    for i in range(mini - 1, maxi + 2):
        for j in range(minj - 1, maxj + 2):
            index = 0
            for di in range(i - 1, i + 2):
                for dj in range(j - 1, j + 2):
                    # bit operations
                    index = index << 1 | \
                            (int((di, dj) in pixel) if (mini <= di <= maxi and minj <= dj <= maxj) else bit)

            # access to if name main block
            if rule[index]:
                enhanced.add((i, j))

    return enhanced


if __name__ == "__main__":
    with open("input.txt") as f:
        rule, *pix = f.read().split('\n')
    rule = [int(x == '#') for x in rule]

    # converted # or not to ints easier to work with
    pix = set((i, j) for i, row in enumerate(pix) for j, ch in enumerate(row) if ch == '#')

    iterations = 50
    for i in range(iterations):
        pix = iterate(pix, i & 1 & rule[0])

    print(len(pix))
