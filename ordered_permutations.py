from itertools import permutations

N = int(input())
R = input()


def check_order(order, R):
    i = 0
    for r in R:
        if r == "<" and order[i] > order[i + 1]:
            return False
        elif r == ">" and order[i] < order[i + 1]:
            return False
        i += 1
    return True


# get the all the permutations of R
count = 0
for order in permutations(range(1, N + 1), N):
    if check_order(order, R):
        count += 1

print(count)
