def find_number_at_index(lines, i, j):
    start = j
    stop = j

    while start >= 0 and lines[i][start].isdigit():
        start -= 1
    start += 1 # because we went one too far

    while stop < len(lines[i]) and lines[i][stop].isdigit():
        stop += 1
    # we don't subtract 1 as the substring function is exclusive
    return start, stop

ADJ_DIRECTIONS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

if __name__ == "__main__":
    filename = "input.txt"
    # filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()
        # grid = [list(line.rstrip('\n')) for line in lines]
        lines = [line.strip('\n') for line in lines]

    symbol_coords = []
    gear_ratios = []
    for row_index, row in enumerate(lines):
        for col_index, char in enumerate(row):
            if char == '*':
                visited = []
                numbers = []
                for direction in ADJ_DIRECTIONS:
                    i, j = row_index, col_index
                    i += direction[0]
                    j += direction[1]
                    if 0 <= i < len(lines) and 0 <= j < len(lines[i]) and lines[i][j].isdigit() and (i, j) not in visited:
                        start, stop = find_number_at_index(lines, i, j)
                        numbers.append(int(lines[i][start:stop]))
                        visited.extend([(i, j) for j in range(start, stop)])
                if len(numbers) == 2:
                    gear_ratios.append(numbers[0] * numbers[1])
    print(sum(gear_ratios))
