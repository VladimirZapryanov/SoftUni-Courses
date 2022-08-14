from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


nodes_count = int(input())
edges_count = int(input())

graph = []
for _ in range(edges_count):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append(Edge(source, destination, weight))

start = int(input())
target = int(input())

distance = [float('inf')] * (nodes_count + 1)
parent = [None] * (nodes_count + 1)
distance[start] = 0

for _ in range(nodes_count - 1):
    update = False
    for edge in graph:
        if distance[edge.source] == float('inf'):
            continue
        new_distance = distance[edge.source] + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source
            update = True

    if not update:
        break

for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.destination]:
        print('Negative Cycle Detected')
        break

else:
    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]

    print(*path, sep=' ')
    print(distance[target])
