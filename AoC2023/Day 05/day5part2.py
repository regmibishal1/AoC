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
    # filename = "input.txt"
    filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()
        sections = ''.join(lines).strip().split('\n\n')

    sects = {"seed": 0, "soil": 0,"fertilizer": 0,"water": 0,"light": 0,"temperature": 0,"humidity": 0,"location": 0}

    # Parse the mapping string
    seeds_parsed = [int(val) for val in lines[0].strip('\n').split(' ')[1:]]
    seeds = set()
    for seed in range(0, len(seeds_parsed), 2):
        seeds.update(list(range(seeds_parsed[seed], seeds_parsed[seed] + seeds_parsed[seed + 1])))

    mappings = defaultdict(lambda: sects.copy())
    min_location = float('inf')
    for seed in seeds:
        mappings[seed]["seed"] = seed
        sects_list = list(sects.keys())
        for index, sect in enumerate(sects_list[:-1]):
            mappings[seed][sects_list[index + 1]] = find_number(mappings[seed][sects_list[index]], parse_mapping_string(sections[index + 1]))
        if mappings[seed]["location"] < min_location:
            min_location = mappings[seed]["location"]
        del mappings[seed]
    print(min_location)

#Part 1  525792406
#Part 2  79004094





