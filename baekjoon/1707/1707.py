import collections
import sys
from collections import deque

input = sys.stdin.readline


def dfs(start):
    need_visited = deque([start])

    while need_visited:
        node = need_visited.pop()
        for adj in graph[node]:
            if visited[adj] == 0: # 인접 노드가 아직 방문 안한 곳
                visited[adj] = -visited[node] # 다른 색으로!
                need_visited.append(adj) # need_visited에 넣어서 dfs 탐색 수행
            elif visited[adj] == visited[node]:
                return False    # 색이 같다면 false.
    return True # 다 돌아서 문제 없으면 True


n = int(input())

# 각 try마다 시행한다.
for _ in range(n):
    node_num, edge_num = map(int, input().split())
    graph = [[] for _ in range(node_num + 1)]  # 리스트로 구현
    visited = [0]*(node_num + 1)    # default값을 0으로 설정

    for i in range(edge_num):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = []
    color = 1   # default 색 값을 1로 놓는다.

    # 각 노드에 대해 visited == 0이면 dfs 수행(연결 요소가 하나가 아닐수도 있어서)
    for node in range(1, node_num+1):
        if visited[node] == 0:
            visited[node] = color # 이 그래프의 첫 색은 1이다.
            result.append(dfs(node)) # dfs 수행한다.

    if False in result:
        print('NO')
    else:
        print('YES')

