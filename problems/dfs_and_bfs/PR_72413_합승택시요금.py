from collections import defaultdict
import sys, heapq

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for node1, node2, fare in fares:
        graph[node1].append([node2, fare])
        graph[node2].append([node1, fare])
    
    costs = [[] for _ in range(n+1)]

    for i in range(1, n+1):
        costs[i] = dijkstra(graph, i)
    
    min_cost = sys.maxsize
    for i in range(1, n+1):
        cost = costs[s][i] + costs[i][a] + costs[i][b]
        min_cost = min(cost, min_cost)
    
    return min_cost

def dijkstra(graph, start):
    INF = sys.maxsize
    cost = [INF] * (n + 1)
    cost[start] = 0

    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        cur_cost, cur = heapq.heappop(heap)
        if cost[cur] < cur_cost:
            continue

        cost[cur] = cur_cost
        for adj, adj_cost in graph[cur]:
            if cost[adj] > cost[cur] + adj_cost:
                cost[adj] = cost[cur] + adj_cost
                heapq.heappush(heap, [cost[adj], adj])
    
    return cost
    


n, s, a, b = 7,3,4,1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

print(solution(n, s, a, b, fares))
