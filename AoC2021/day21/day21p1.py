
if __name__ == "__main__":
    player1, player2 = [9, 3]
    scoreP1, scoreP2 = 0, 0
    offset = 0
    count = 0
    final = None
    while not final:
        step1, step2, step3 = offset % 100, (offset+1) % 100, (offset+2) % 100
        newPos = (player1 + step1 + step2 + step3 + 2) % 10+1
        offset = (offset+3) % 100
        count += 3
        scoreP1 += newPos
        if scoreP1 >= 1000:
            final = scoreP2 * count
        player1, player2, scoreP1, scoreP2 = player2, newPos, scoreP2, scoreP1

    print(final)
