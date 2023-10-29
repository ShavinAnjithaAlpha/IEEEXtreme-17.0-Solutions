import heapq

N = int(input())
cities = {}
roads = []
i = 0

for _ in range(N):
    a, b, c = input().split(" ")
    c = int(c)
    if cities.get(a, -1) == -1:
        cities[a] = i
        i += 1

    if cities.get(b, -1) == -1:
        cities[b] = i
        i += 1

    roads.append((c, cities[a], cities[b]))
    roads.append((c, cities[b], cities[a]))


# prims algorithm for finding the minimum spanning tree
mst = set([0, ])
mst_edges = []
cost = 0

while len(mst) != len(cities.keys()):
    # get the neighboring edges
    neighbors = []
    for m in mst:
        for road in roads:
            if road[1] == m and road[2] not in mst:
                neighbors.append(road)

    if (neighbors == []):
        print(-1)
        exit(0)

    heapq.heapify(neighbors)
    min_cost = min(neighbors)[0]
    num_min_edges = 0
    for item in roads:
        if item[0] == min_cost:
            num_min_edges += 1
    # get the minimu edge
    min_edge = heapq.heappop(neighbors)
    mst.add(min_edge[2])
    mst_edges.append(min_edge)
    cost += min_edge[0] * num_min_edges

print(cost // 2)
