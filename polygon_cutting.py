(N, M) = list(map(int, input().split(" ")))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y


class Edge:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __eq__(self, __value: object) -> bool:
        return self.p1 == __value.p1 and self.p2 == __value.p2 or self.p1 == __value.p2 and self.p2 == __value.p1


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def triangle_area(self):
        """
        Calculates the square area of the triangle using the formula:
        area = 0.5 * |(x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)|
        """
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = self.p3.x, self.p3.y

        area = abs((x1 * y2 + x2 * y3 + x3 * y1) -
                   (y1 * x2 + y2 * x3 + y3 * x1))

        return area


def is_valid(t1, t2):
    edges1 = [Edge(t1.p1, t1.p2), Edge(t1.p2, t1.p3), Edge(t1.p3, t1.p1)]
    edges2 = [Edge(t2.p1, t2.p2), Edge(t2.p2, t2.p3), Edge(t2.p3, t2.p1)]

    # check whether there share a common edge
    for e1 in edges1:
        for e2 in edges2:
            if e1 == e2:
                return False
    return True


# node list
nodes = []
edges = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    (x, y) = list(map(int, input().split(" ")))
    nodes.append(Point(x, y))
    if (i < N - 1):
        edges[i][i + 1] = True
        edges[i + 1][i] = True

edges[N - 1][0] = True
edges[0][N - 1] = True

for _ in range(M):
    (i, j) = list(map(int, input().split(" ")))
    edges[i - 1][j - 1] = True
    edges[j - 1][i - 1] = True


areas = []
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if edges[i][j] and edges[j][k] and edges[k][i]:
                areas.append(
                    Triangle(nodes[i], nodes[j], nodes[k]))


def find_optimal_area(areas):

    def validity(index, fil_areas):
        for ar in fil_areas:
            if not is_valid(areas[index], areas[ar]):
                return False
        return True

    """
    Finds the optimal total area of non-overlapping triangles given a list of areas.
    """
    # Sort the areas in descending order
    areas.sort(reverse=True, key=lambda x: x.triangle_area())

    # Initialize the total area to 0
    total_area = 0

    # loop through the areas and find the optimal total area in which each two triangle don't share a commong edge
    filtered_areas = []
    # used = [False] * len(areas)
    for i in range(0, len(areas)):
        if validity(i, filtered_areas):
            filtered_areas.append(i)
            # used[i] = True

    for a in filtered_areas:
        total_area += areas[a].triangle_area()

    return total_area


# for t in areas:
    # print(t.triangle_area())
# print("============")
print(find_optimal_area(areas))
