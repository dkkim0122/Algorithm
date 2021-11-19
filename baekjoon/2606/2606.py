from collections import deque
import sys
input = sys.stdin.readline

node_num = int(input().strip())
edge_num = int(input().strip())

graph = [[] for _ in range(node_num + 1)]

for i in range(edge_num):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(node_num + 1)


def dfs(start):
    need_visited = deque([start])

    while need_visited:
        node = need_visited.pop()
        for i in graph[node]:
            if visited[i] == 0:
                need_visited.append(i)
                visited[i] = 1

dfs(1)
print(sum(visited)-1)
