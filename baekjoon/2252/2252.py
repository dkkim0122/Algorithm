# 키의 순서를 일부 비교한 데이터가 있다
# 서로의 순서를 일부 알고 있으므로 위상정렬을 이용해서 순서를 판단할 수 있다.

import sys
from collections import deque

def topology_sort():
    result = []
    queue = deque()

    for i in range(1, node_num+1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        now = queue.popleft()
        result.append(now)
        for adj in graph[now]:
            indegree[adj] -= 1
            if indegree[adj] == 0:
                queue.append(adj)
    return result

if __name__=='__main__':
    input = sys.stdin.readline

    node_num, edge_num = map(int, input().split())
    graph = [[] for _ in range(node_num+1)] 
    indegree = [0] * (node_num+1)

    for i in range(edge_num):
        start, end = map(int, input().split())
        graph[start].append(end)
        indegree[end] += 1

    # print(graph)
    # print(indegree)

    print(*topology_sort())