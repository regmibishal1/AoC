import re

if __name__ == "__main__":
    # filename = "input.txt"
    filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()
        lines =  [line.strip('\n').split(':')[1].split('|') for line in lines]

    cards = [1] * len(lines)
    for card_index, card in enumerate(lines):
        winning_nums = [int(num) for num in re.findall(r'\d+', card[0])]
        card_nums = [int(num) for num in re.findall(r'\d+', card[1])]
        same = set(card_nums).intersection(winning_nums)

        for row in range(card_index + 1, min(card_index + 1 + len(same), len(lines))):
            cards[row] += cards[card_index]

    print(cards)
    print(sum(cards))
