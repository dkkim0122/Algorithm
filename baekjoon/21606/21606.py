import sys
from collections import deque
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

def dfs(start):
    visited = []
    visited.append(start)
    need_visit = deque([start])

    while need_visit:
        node = need_visit.pop()
        for adj in graph[node]:
            if adj not in visited:
                visited.append(adj)
                if in_out[adj] == 0:
                    need_visit.append(adj)
                elif in_out[adj] == 1:
                    path.append(visited)
                    # adj 하나에서 return까지 가면 다른 adj는 못 본다.


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

print(len(path))