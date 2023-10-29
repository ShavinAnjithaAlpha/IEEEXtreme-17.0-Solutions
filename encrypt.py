n = int(input())


def encrypt(text, shift):
    new_text = ""
    for i in text:
        if i != ' ' and i != '.' and i != ',' and i != '!' and i != '?' and i != ';' and i != '\n':
            new_text += left_shift(i, shift)
        else:
            new_text += i

    return new_text


def decrypt(text, shift):
    new_text = ""
    for i in text:
        if i != ' ' and i != '.' and i != ',' and i != '!' and i != '?' and i != ';' and i != '\n':
            new_text += right_shift(i, shift)
        else:
            new_text += i

    return new_text


def left_shift(c, shift):
    # get the ord value of character
    x = ord(c) - ord('a')
    x = (x - shift)
    if (x < 0):
        x %= -26
    else:
        x %= 26
    if (x < 0):
        return chr(x + 26 + ord('a'))
    return chr(x + ord('a'))


def right_shift(c, shift):
    x = ord(c) - ord('a')
    x += shift
    x %= 26
    return chr(x + ord('a'))


for _ in range(n):
    shift = int(input())
    text = input()[:-1]

    if (" the " in text):
        print(encrypt(text, shift))
    else:
        print(decrypt(text, shift))
