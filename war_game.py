from collections import deque
N = int(input())


def create_deck(cards):
    d = deque()
    for card in cards:
        if (card not in ['T', 'J', 'Q', 'K', 'A']):
            d.append(int(card))
        else:
            if (card == 'T'):
                d.append(10)
            elif (card == 'J'):
                d.append(11)
            elif (card == 'Q'):
                d.append(12)
            elif (card == 'K'):
                d.append(13)
            else:
                d.append(14)

    return d


def play(player1, player2):

    while (True):
        # get the top cards from both players
        p1 = player1.popleft()
        p2 = player2.popleft()
        if (p1 > p2):
            player1.append(p2)
        elif (p2 > p1):
            player2.append(p1)
        else:
            player1.append(p1)
            player2.append(p2)

        if (len(player1) == 0):
            print("player 2")
            break
        elif (len(player2) == 0):
            print("player 1")
            break
        elif (len(player1) == 0 and len(player2) == 0):
            print("draw")
            break
        elif (player1 == player2):
            print("draw")
            break


for _ in range(N):

    pl1 = input().split()
    pl2 = input().split()

    player1 = create_deck(pl1)
    player2 = create_deck(pl2)

    play(player1, player2)
