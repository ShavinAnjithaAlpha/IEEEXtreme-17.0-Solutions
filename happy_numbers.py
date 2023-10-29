(a, b) = tuple(map(int, input().split(" ")))

happy_table = set([1, 7, 10, 13])
unhappy_numbers = set([2, 3, 4, 5, 6, 8, 9, 11, 12])


def value(n):
    n_str = str(n)
    val = 0
    for i in n_str:
        val += int(i) ** 2
    return val


def is_happy(n):
    if n in happy_table:
        return True
    elif n in unhappy_numbers:
        return False
    else:
        x = n
        tmp = [n]
        while (True):
            x = value(x)
            tmp.append(x)
            if (x in unhappy_numbers):
                unhappy_numbers.update(tmp)
                return False
            if x in happy_table:
                happy_table.update(tmp)
                return True


count = 0
for i in range(a, b + 1):
    if (is_happy(i)):
        count += 1

print(count)
