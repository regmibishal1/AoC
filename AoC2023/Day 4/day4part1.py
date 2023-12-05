import re

if __name__ == "__main__":
    filename = "input.txt"
    # filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()
        lines =  [line.strip('\n').split(':')[1].split('|') for line in lines]

    winnings = []
    for card_index, card in enumerate(lines):
        winning_nums = [int(num) for num in re.findall(r'\d+', card[0])]
        card_nums = [int(num) for num in re.findall(r'\d+', card[1])]
        matches = 0
        same = set(card_nums).intersection(winning_nums)
        winnings.append(pow(2, len(same) - 1)if len(same) > 0 else 0)

    print(sum(winnings))



