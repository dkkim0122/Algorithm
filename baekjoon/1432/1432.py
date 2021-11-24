import sys
from collections import defaultdict, deque
import heapq


def topology_sort():
    # 만약 level이 같은 값이 있을 때 사전 순서대로 저장하기 위해 max heap을 사용한다
    queue = []

    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(queue, -i)
    
    # 새로운 리스트 ans에 각 노드가 힙에서 빠져나가는 순서를 기록한다
    N = n
    while queue:
        start = -heapq.heappop(queue)
        ans[start] = N
        for adj in back_graph[start]:
            indegree[adj] -= 1
            if indegree[adj] == 0:
                heapq.heappush(queue, -adj)
        N -= 1


if __name__=='__main__':
    input = sys.stdin.readline

    n = int(input())

    # 가장 큰 숫자부터 정렬을 해 주어야 맞다고 하더라...
    # 그러기 위해서 백그래프 활용
    back_graph = defaultdict(list)
    indegree = [0] * (n + 1)
    ans = [0] * (n + 1) # 각 인덱스에 해당하는 노드들이 위상 정렬되는 순서를 저장한다.

    matrix = [[0] for _ in range(n+1)]
    for i in range(1, n+1):
        matrix[i].extend(list(map(int, input().strip())))
        for j in range(1, n+1):
            if matrix[i][j] == 1:
                back_graph[j].append(i) # 값이 큰 순서부터 보아야 한다고 한다.
                indegree[i] += 1

    topology_sort()
    
    if ans.count(0) > 1:
        print(-1)
    else:
        print(*ans[1:])
