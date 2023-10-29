import matplotlib.pyplot as plt
(n, h0, a, c, q) = list(map(int, input().split(" ")))

heights = [h0]
for i in range(n - 1):
    heights.append((heights[i] * a + c) % q)

plt.plot(heights)
plt.xlabel('Person')
plt.ylabel('Height')
plt.title('Heights of People in Line')
plt.show()
# END: 8f7d6h3j4k5l

noticable_peoples = 0
# max_height = heights[0]
for i in range(1, n):
    max_height = heights[i - 1]
    noticable_peoples += 1
    for j in range(i - 1, -1, -1):
        if max_height < heights[j]:
            noticable_peoples += 1
            max_height = heights[j]

print(noticable_peoples)
