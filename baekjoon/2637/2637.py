# 위상 정렬로 어떻게 풀지..?
# dp로 어떻게 풀지..?

import sys
from collections import deque

def topology_sort():
    while queue:
        node = queue.popleft()
        for adj in graph[node]:
            start, end, cost = adj  # graph[start] = (start, end, cost)
            costs_list[end] += costs_list[node]*cost  # cost 계산
            indegree[end] -= 1
            if indegree[end] == 0:
                queue.append(end)


if __name__=='__main__':
    input = sys.stdin.readline

    node_num = int(input())
    edge_num = int(input())

    graph = [[] for _ in range(node_num + 1)]
    indegree = [0] * (node_num + 1)
    costs_list = [0] * (node_num + 1)
    costs_list[node_num] = 1 # 완제품의 cost를 1로 잡고 시작

    for i in range(edge_num):
        start, end, num = map(int,input().split())
        graph[start].append((start, end, num))
        indegree[end]+=1

    queue = deque()
    for i in range(1, node_num+1):
        if indegree[i] == 0:
            queue.append(i)

    # print(queue)
    topology_sort()

    for i in range(1,node_num+1):  # 그래프에서 indegree가 0인, 즉 기본 부품들
        if graph[i] == []:
            print(i, costs_list[i])