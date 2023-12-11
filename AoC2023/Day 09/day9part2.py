if __name__ == "__main__":
    filename = "input.txt"
    # filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()

    lines = [list(map(int, x.strip('\n').split(' '))) for x in lines]

    total = 0
    for line in lines:
        history = [line]
        while not all(val == 0 for val in history[-1]):
            diff_sequence = [history[-1][i + 1] - history[-1][i] for i in range(len(history[-1]) - 1)]
            history.append(diff_sequence)
        val = 0

        for i in history[::-1]:
            val = i[0] - val
        total += val
    print(total)
