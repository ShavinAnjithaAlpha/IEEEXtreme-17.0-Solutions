import heapq

list1 = [1, 7, 10, 4, 2, 3, 0]

heapq.heapify(list1)

print(list1)

print("smallest: ", heapq.heappop(list1))
print("second smallest: ", heapq.heappop(list1))

# push values to the heap
heapq.heappush(list1, 6)
print(list1)

print("largest 3 items: ", heapq.nlargest(3, list1))
