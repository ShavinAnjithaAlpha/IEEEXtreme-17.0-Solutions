from collections import *

# Counter is a dict subclass for counting hashable objects
list1 = [1, 2, 3, 4, 1, 2, 6, 7, 3, 8, 9, 0, 1, 2, 3]
counter = Counter(list1)

for key, count in counter.items():
    print(f"{key} : {count}")

print(counter.most_common(2))
