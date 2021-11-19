import collections
import sys
from collections import deque

input = sys.stdin.readline

num_node, num_edge = map(int, input().split())
graph=[[] for i in range(num_node + 1)]

for i in range(num_node):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(num_node + 1)

def bfs(start_node):
    need_visited = deque()
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                need_visited.append(i)


count = 0
for i in range(1, num_node+1):
    if visited[i] == 0:
        bfs(i)
        count += 1

print(count)