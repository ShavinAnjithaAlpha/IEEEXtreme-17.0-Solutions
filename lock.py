import heapq
import bisect


def int_to_str(num, digits):
    if (len(str(num)) > digits):
        return str(num)[len(str(num)) - digits:]

    num_str = str(num)
    if len(num_str) < digits:
        num_str = "0" * (digits - len(num_str)) + num_str
    return num_str


def is_one_digit_change(str_num1, str_num2):
    if len(str_num1) != len(str_num2):
        return False

    num_differences = 0

    for digit1, digit2 in zip(str_num1, str_num2):
        if digit1 != digit2:
            diff = abs(int(digit1) - int(digit2))
            ch = (digit1 == "0" and digit2 == "9") or (
                digit2 == "0" and digit1 == "9")
            if (diff != 1 and not ch):
                return False
            else:
                num_differences += 1
                if num_differences > 1:
                    return False

    return num_differences == 1


def generate_sequence(n, h0, a, b, q):
    l = set([h0])
    h = h0
    while True:
        h = (a*h + b) % q
        if h in l:
            break
        else:
            l.add(h)

    l = list(l)
    l.sort()

    l_str = []
    for j in range(len(l)):
        f = int_to_str(l[j], n)
        if f != -1:
            l_str.append(f)

    l_str.sort()
    return l_str


def dijkstra(start, end, graph, nodes):
    # initialize distances to infinity for all nodes except start node
    distances = {node: float('inf') for node in range(len(nodes))}
    distances[start] = 0
    num_paths = {node: 0 for node in range(len(nodes))}
    num_paths[start] = 1
    visited = [False for _ in range(len(nodes))]
    visited[start] = True

    heap = [(0, start)]
    heapq.heapify(heap)

    while heap:
        # get the min distance node
        (dist, node) = heapq.heappop(heap)

        # if we've reached the end node, return the distance
        if node == end:
            return dist, num_paths[node]

        # loop through the neighbors of the current node
        for neighbor in range(len(graph[node])):
            # if the neighbor is not connected to the current node, skip it
            if not graph[node][neighbor]:
                continue

            if visited[neighbor]:
                continue

            # calculate the distance to the neighbor
            new_dist = dist + 1

            # if the new distance is less than the current distance to the neighbor, update the distance
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
                num_paths[neighbor] = num_paths[node]
            elif new_dist == distances[neighbor]:
                num_paths[neighbor] += num_paths[node]
        visited[node] = True

    # if we've exhausted all nodes and haven't reached the end node, return -1
    return -1


T = int(input())
for _ in range(T):
    (n, t, h_0, a, b, q) = list(map(int, input().split(" ")))
    seq = generate_sequence(n, h_0, a, b, q)
    nodes = [int_to_str(0, n), ]
    nodes.extend(seq)
    end = bisect.bisect_left(nodes, int_to_str(t, n))
    bisect.insort_left(nodes, int_to_str(t, n))

    print(nodes)
    edges = [[False for _ in range(len(nodes))] for _ in range(len(nodes))]
    # create the edge graph based on the sequence
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if is_one_digit_change(nodes[i], nodes[j]):
                edges[i][j] = True
                edges[j][i] = True
                # print("edge: ", nodes[i], nodes[j])

    result = dijkstra(0, end, edges, nodes)
    if result != -1:
        print(result[0], result[1])
    else:
        print(-1)
