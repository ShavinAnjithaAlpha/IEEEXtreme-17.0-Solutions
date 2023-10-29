import bisect

numbers = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4]

print(f"position to insert 2 in the list: {bisect.bisect(numbers, 2)}")
print(f"position to insert 4 in the list: {bisect.bisect(numbers, 4)}")

# insert the item into the sorted list
bisect.insort(numbers, 2)
print(numbers)

bisect.insort_left(numbers, 4)
print(numbers)
