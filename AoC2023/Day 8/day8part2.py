from collections import defaultdict
import math


def calc_steps(node, sequence, network):
    current_node = node
    index = 0

    while not current_node.endswith('Z'):
        instruction = sequence[index%len(sequence)]
        current_node = network[current_node][0 if instruction == 'L' else 1]
        index += 1
    return index


if __name__ == "__main__":
    filename = "input.txt"
    # filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()

    instructions = list(lines[0].strip())

    ending_A_nodes = set()
    directions = defaultdict(tuple)
    for inst in lines[2:]:
        key, value = inst.split(' = ')
        parsed_value = tuple(value.strip('()\n').split(', '))
        directions[key] = parsed_value

        if key.endswith('A'):
            ending_A_nodes.add(key)

    steps = []
    for node in ending_A_nodes:
        steps.append(calc_steps(node, instructions, directions))

    print(f"steps: {math.lcm(*steps)}")







