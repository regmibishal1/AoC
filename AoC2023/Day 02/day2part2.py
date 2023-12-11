import re


if __name__ == "__main__":
    filename = "input.txt"
    # filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()

    id_pattern = r"Game\s+(\d+)"
    color_pattern = r"(\d+)\s+([a-zA-Z\s,]+)"

    power_sets = []
    for line in lines:
        game_info = line.split(':')
        game_id = int(re.findall(id_pattern, game_info[0].strip())[0])
        game_output = game_info[1].strip().split(';')

        min_vals = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for output in game_output:
            matches = re.findall(color_pattern, output)
            for match in matches:
                amount = int(match[0])
                color = match[1].strip().strip(",").lower()
                if amount > min_vals[color]:
                    min_vals[color] = amount
        power_set = min_vals['red'] * min_vals['green'] * min_vals['blue']
        power_sets.append(power_set)

    print(sum(power_sets))

