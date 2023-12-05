import re

MAX_VALUES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

if __name__ == "__main__":
    filename = "input.txt"
    # filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()

    id_pattern = r"Game\s+(\d+)"
    color_pattern = r"(\d+)\s+([a-zA-Z\s,]+)"

    possbile_games = []
    for line in lines:
        game_info = line.split(':')
        game_id = int(re.findall(id_pattern, game_info[0].strip())[0])
        game_output = game_info[1].strip().split(';')

        valid = True
        for output in game_output:
            matches = re.findall(color_pattern, output)
            for match in matches:
                amount = int(match[0])
                color = match[1].strip().strip(",").lower()
                if amount > MAX_VALUES[color]:
                    valid = False
                    break

        if valid:
            possbile_games.append(game_id)

    print(sum(possbile_games))

