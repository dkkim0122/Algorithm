import sys
from collections import deque
sys.setrecursionlimit(10**5)


input = sys.stdin.readline

def dfs(start, visited = []):
      # 각 dfs마다 visited를 따로 돌린다 -> 모든 노드 시작점에 대해 탐색을 각각 해야 하므로
    visited.append(start)

    for adj in graph[start]:
        if adj not in visited: # 방문한 적 없다.
            if in_out[adj] == 1:  # 방문한 적 없고, 실외면 끝낸다.
                visited.append(adj)
                path.append(visited)
            else:
                dfs(adj, visited) # 실내면 거기서부터 다시 실외로 가는 방법 찾기


n = int(input())
in_out = [0] # 0번째 인덱스는 무시
graph = [[] for _ in range(n+1)]

for i in input().strip():
    in_out.append(int(i))

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

path = []

for i in range(1, n+1):
    if in_out[i] == 1:  # 실외일 때만 실행한다.
        dfs(i, [])

print(len(path))