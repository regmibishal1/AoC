from functools import cache
from itertools import product


@cache
def simulate(player1, player2, scoreP1=0, scoreP2=0):
    if scoreP1 >= 21:
        return 1, 0
    if scoreP2 >= 21:
        return 0, 1

    countP1, countP2 = 0, 0
    for step1, step2, step3 in allRolls:
        newPos = (player1 + step1 + step2 + step3) % 10
        score = scoreP1 + newPos + 1
        player2Win, player1Win = simulate(player2, newPos, scoreP2, score)
        countP1 += player1Win
        countP2 += player2Win

    return countP1, countP2


if __name__ == "__main__":
    allRolls = list(product([1, 2, 3], repeat=3))
    player1, player2 = [8, 2]
    print(max(simulate(player1, player2)))
