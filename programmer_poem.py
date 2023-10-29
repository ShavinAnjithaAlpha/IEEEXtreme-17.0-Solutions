(N, M) = tuple((map(int, input().split(" "))))

rhymes = []
for _ in range(N):
    rhymes.append(input().split(" "))

input()
poem = []
for _ in range(M):
    poem.append(input().split(" "))


def in_rhyme(word, rhymes):
    for i in range(len(rhymes)):
        if word.lower() in rhymes[i]:
            return i
    return -1


c_map = {}
C = 'A'
for i, line in enumerate(poem):
    # get the last word
    last_words = []
    if i == 0:
        last_words.append(line[-1])
        last_words.append(poem[i + 1][-1])
    elif i == len(poem) - 1:
        last_words.append(poem[i - 1][-1])
        last_words.append(line[-1])
    else:
        last_words.append(poem[i - 1][-1])
        last_words.append(line[-1])
        last_words.append(poem[i + 1][-1])

    # check whether last words are in a rhymes class
    p = in_rhyme(last_words[0], rhymes)
    q = in_rhyme(last_words[1], rhymes)
    r = -1
    if (len(last_words) == 3):
        r = in_rhyme(last_words[2], rhymes)

    # print(last_words)
    # print(p, q, r)
    if (r == -1):
        if (p == -1 or q == -1):
            print("X", end="")
        elif (p == q):
            if not c_map.get(p, False):
                c_map[p] = C
                print(C, end="")
                C = chr(ord(C) + 1)
            else:
                print(c_map.get(p), end="")
    else:
        if (p == q == r):
            print(c_map.get(p), end="")
        elif (p == q):
            # print("p == q: ", last_words)
            print(c_map.get(p), end="")
        elif (q == r):
            # print("q == r: ", last_words)
            if not c_map.get(q, False):
                c_map[q] = C
                print(C, end="")
                C = chr(ord(C) + 1)
            else:
                print(c_map.get(q), end="")
        else:
            print("X", end="")
    # print(c_map)
