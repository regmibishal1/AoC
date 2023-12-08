from collections import defaultdict

def calc_steps(sequence, network):
    current_node = 'AAA'
    steps = 0
    index = 0

    while True:
        instruction = sequence[index]
        current_node = network[current_node][1 if instruction == 'R' else 0]
        steps += 1

        if current_node == 'ZZZ':
            return steps
        index = (index + 1) % len(sequence)

if __name__ == "__main__":
    filename = "input.txt"
    # filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()

    instructions = list(lines[0].strip())

    directions = defaultdict(tuple)
    for inst in lines[2:]:
        key, value = inst.split(' = ')
        parsed_value = tuple(value.strip('()\n').split(', '))
        directions[key] = parsed_value

    print(f"steps: {calc_steps(instructions, directions)}")







