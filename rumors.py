N = int(input())
rels = []
for _ in range(N):
    rels.append(input().split(" "))


# create the nodes
nodes = {}
edges = {}
i = 0
for src, sym, res in rels:
    if not nodes.get(src, False):
        nodes[src] = i
        i += 1
    if not nodes.get(res, False):
        nodes[res] = i
        i += 1

    if sym == "->":
        if (not edges.get(nodes[src], False)):
            edges[nodes[src]] = []
        edges[nodes[src]].append(nodes[res])
    else:
        if (not edges.get(nodes[src], False)):
            edges[nodes[src]] = []
        if (not edges.get(nodes[res], False)):
            edges[nodes[res]] = []
        edges[nodes[src]].append(nodes[res])
        edges[nodes[res]].append(nodes[src])


nodes_ = [True for _ in range(len(nodes))]
directed_nodes = []
# remove directed nodes
for key in edges.keys():
    for node in edges[key]:
        if not edges.get(node, False):
            nodes_[node] = False
            directed_nodes.append(node)
            continue
        if key not in edges[node]:
            nodes_[node] = False
            directed_nodes.append(node)

while directed_nodes != []:
    tmp = []
    for key in directed_nodes:
        if not edges.get(key, False):
            continue
        for node in edges[key]:
            nodes_[node] = False
            if nodes_[node]:
                tmp.append(node)
    directed_nodes = tmp


for index in range(len(nodes_)):
    if nodes_[index]:
        # get the name of the person through nodes dictionary
        for key, value in nodes.items():
            if value == index:
                print(key)
                break
