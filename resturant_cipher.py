from collections import Counter

N = int(input())
secret_messages = []

for _ in range(N):
    secret_messages.append(input())


def decrypt(secret_messages):
    for message in secret_messages:
        # count the number of occurence
        count = Counter(message.replace(" ", ""))
        new_counter = {}
        for k in count.keys():
            if k.lower() in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
                new_counter[k] = count[k]
        # get the most common character
        most_common = Counter(new_counter).most_common(1)
        # capitalize the most common character
        print(most_common[0][0].upper())


decrypt(secret_messages)
