import collections
import sys
from collections import deque

input = sys.stdin.readline

num_node, num_edge = map(int, input().split())
graph = collections.defaultdict(list)

for i in range(num_edge):
    node1, node2 = map(int, input().split())

    graph[node1].append(node2)
    graph[node2].append(node1)

def bfs(graph, start_node):
    visited = []
    need_visited = deque()
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.popleft()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    
    return visited

count = 1
result = bfs(graph, next(iter(graph)))
for i in range(1, num_node+1):
    if i not in result:
        result.extend(bfs(graph, i))
        count += 1

print(count)