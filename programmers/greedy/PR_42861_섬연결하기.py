from collections import defaultdict
import sys, heapq

def solution(n, costs):
    graph = defaultdict(list)
    for land1, land2, cost in costs:
        graph[land1].append([cost, land2])
        graph[land2].append([cost, land1])
    
    max_list = []
    for i in range(n):
        result = dijkstra(i, graph, n)
        if result != 0:
            max_list.append(result)

    return min(max_list)

def dijkstra(start, graph, n):
    INF = sys.maxsize
    cost_list = [[INF, 0] for _ in range(n)]
    heap = []

    cost_list[start] = [0, 1]
    heapq.heappush(heap, (cost_list[start], start, 1))

    while heap:
        cur_cost, cur, count = heapq.heappop(heap)
        if cost_list[cur][0] < cur_cost[0]:
            continue

        cost_list[cur][0] = cur_cost[0]
        for adj_cost, adj in graph[cur]:
            new_cost = cur_cost[0] + adj_cost
            if new_cost < cost_list[adj][0]:
                cost_list[adj] = [new_cost, count+1]
                heapq.heappush(heap, (cost_list[adj], adj, count+1))
    max = 0
    print(cost_list)
    for cost, count in cost_list:
        if count == n and cost > max:
            max = cost
    return max

n = 4
costs = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]]

print(solution(n, costs))
