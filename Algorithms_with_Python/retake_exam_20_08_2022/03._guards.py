from collections import deque

nodes = int(input())
edges = int(input())

graph = {}
for n in range(1, nodes + 1):
    graph[n] = []


for _ in range(edges):
    node, connection = [int(x) for x in input().split()]
    graph[node].append(connection)


start_node = int(input())
visited = set()
visited.add(start_node)


queue = deque()
queue.append(start_node)
while queue:
    current_node = queue.popleft()
    visited.add(current_node)

    if len(graph[current_node]) != 0:
        for child in graph[current_node]:
            if child not in visited:
                queue.append(child)


not_visited = sorted(set(graph.keys()).difference(visited))
print(*not_visited, sep=' ')