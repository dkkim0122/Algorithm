# 위상 정렬로 어떻게 풀지..?
# dp로 어떻게 풀지..?

import sys
from collections import deque

def topology_sort():
    queue = deque()
    for i in range(1, node_num+1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        node = queue.popleft()
        for adj, cost in graph[node]: # graph[start] = (adj, cost)
            val = 1 if costs_list[node] == 0 else costs_list[node] # 완제품의 cost를 1로 잡고
            costs_list[adj] += val * cost  # cost 계산
            indegree[adj] -= 1
            if indegree[adj] == 0:
                queue.append(adj)


if __name__=='__main__':
    input = sys.stdin.readline

    node_num = int(input())
    edge_num = int(input())

    graph = [[] for _ in range(node_num + 1)]
    indegree = [0] * (node_num + 1)
    costs_list = [0] * (node_num + 1)  # 각 노드 값이 사용된 횟수

    for i in range(edge_num):
        start, end, num = map(int,input().split())
        graph[start].append((end, num))
        indegree[end]+=1

    topology_sort()

    for i in range(1,node_num+1):  # 그래프에서 indegree가 0인, 즉 기본 부품들
        if graph[i] == []:
            print(i, costs_list[i])