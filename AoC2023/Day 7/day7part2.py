from functools import cmp_to_key
from collections import Counter

ORDER = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

def compare_hands(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]

    type1 = hand_type(hand1)
    type2 = hand_type(hand2)

    if type1 != type2:
        return type1 - type2

    for i in range(5):
        if ORDER[hand1[i][0]] != ORDER[hand2[i][0]]:
            return ORDER[hand1[i][0]] - ORDER[hand2[i][0]]

    return 0

def hand_type(hand):
    counts = Counter(hand)
    j_count = counts['J']
    counts = sorted(counts.values(), reverse=True)

    if counts == [5]:
        return 8  # Five of a kind
    elif counts == [4, 1]:
        if j_count != 0:
            return 8  # Five of a kind
        return 7  # Four of a kind
    elif counts == [3, 2]:
        if j_count == 2 or j_count == 3:
            return 8  # Five of a kind
        return 6  # Full house
    elif counts == [3, 1, 1]:
        if j_count == 3 or j_count == 1:
            return 7 # Four of a kind
        return 5  # Three of a kind
    elif counts == [2, 2, 1]:
        if j_count == 2:
            return 7 # Four of a kind
        if j_count == 1:
            return 6 # Full house
        return 4  # Two pair
    elif counts == [2, 1, 1, 1]:
        if j_count == 2 or j_count == 1:
            return 5 # Three of a kind
        return 3  # One pair
    else:
        if j_count == 1:
            return 3 # One pair
        return 2  # High card


if __name__ == "__main__":
    filename = "input.txt"
    # filename = 'input_sample.txt'

    with open(filename) as f:
        lines = f.readlines()

    hands_bids = [(line.strip().split()[0], int(line.strip().split()[1])) for line in lines]
    hands_bids = sorted(hands_bids, key=cmp_to_key(compare_hands))

    total_winnings = 0
    for i, (hand, bid) in enumerate(hands_bids):
        rank = i + 1
        total_winnings += rank * bid
        # print(f"Hand: {hand}, Rank: {rank}")

    print(f"Total Winnings: {total_winnings}")










