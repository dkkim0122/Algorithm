import sys
from collections import deque

input = sys.stdin.readline

def dfs(start):
    visited = [0] * (n+1)
    visited[start] = 1
    need_visit = deque([start])

    while need_visit:
        node = need_visit.pop()
        for adj in graph[node]:
            if visited[adj] == 0:
                visited[adj] = 1
                if in_out[adj] == 0:
                    need_visit.append(adj)
                elif in_out[adj] == 1:
                    path.append(visited)
                    return

    path.append(visited)
    return

n = int(input())
in_out = [0]
graph = [[] for _ in range(n+1)]

for i in input().strip():
    in_out.append(int(i))

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

path = []

for i in range(1, n+1):
    if in_out[i] == 1:
        dfs(i)

print(len(path)*2)