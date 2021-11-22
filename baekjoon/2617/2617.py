import sys
from collections import deque


# 한 노드에 대해 인접한(나보다 무거운/가벼운) 노드의 개수를 세 준다.
def dfs(graph, start):
    visited = [start]
    need_visit = deque()
    need_visit.append(start)
    count = 0 # 인접 노드의 개수

    while need_visit:
        node = need_visit.pop()
        for adj in graph[node]:
            if adj not in visited:
                visited.append(adj)
                need_visit.append(adj)
                count += 1  # 무거운/가벼운 노드가 있을때만

    if count > n//2: # 만약 인접 노드의 개수가 절반보다 많으면
        return True
    else:
        return False


if __name__ == '__main__':
    input = sys.stdin.readline

    n, m = map(int, input().split())

    # 자기보다 무거운/가벼운 대소 비교를 위한 리스트    
    heavier = [[] for _ in range(n+1)]
    lighter = [[] for _ in range(n+1)]
    for i in range(m):
        heavy, light = map(int, input().split())
        lighter[heavy].append(light)
        heavier[light].append(heavy)

    # 전체에서 자기보다 무거운/가벼운 구슬의 개수
    # 자기보다 무거운 구슬보다 무거운 구슬도 자기보다 무거우니까 체크해줘야 한다.
    heavy_num = [0]*(n+1)
    light_num = [0]*(n+1)

    for i in range(1, n+1):
        heavy_num[i] = dfs(heavier, i)
        light_num[i] = dfs(lighter, i)

    print(sum(heavy_num)+sum(light_num))