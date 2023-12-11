import re
from collections import defaultdict

# find number for the seed
def find_number(number, mapping):
    for dest_start, source_start, length in mapping:
        if source_start <= number < source_start + length:
            return dest_start + (number - source_start)
    return number

# used to parse mapping
def parse_mapping_string(mapping_string):
    rows = mapping_string.strip().split('\n')
    parsed_val = []
    for row in rows[1:]:
        parsed_val.append(tuple([int(num) for num in re.findall(r'-?[\d]+', row)]))

    return parsed_val

if __name__ == "__main__":
    filename = "input.txt"
    # filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()
        sections = ''.join(lines).strip().split('\n\n')

    sects = {"seed": 0, "soil": 0,"fertilizer": 0,"water": 0,"light": 0,"temperature": 0,"humidity": 0,"location": 0}

    # Parse the mapping string
    seeds = [int(val) for val in lines[0].strip('\n').split(' ')[1:]]
    mappings = defaultdict(lambda: sects.copy())

    for seed in seeds:
        mappings[seed] = sects.copy()
        mappings[seed]["seed"] = seed

    for seed in seeds:
        sects_list = list(sects.keys())
        for index, sect in enumerate(sects_list[:-1]):
            mappings[seed][sects_list[index + 1]] = find_number(mappings[seed][sects_list[index]], parse_mapping_string(sections[index + 1]))

    print(mappings)

    location = []
    for val in mappings.values():
        location.append(val["location"])

    print(min(location))

#Part 1  525792406
#Part 2  79004094





