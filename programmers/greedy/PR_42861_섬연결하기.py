from collections import defaultdict
import sys, heapq

def solution(n, costs):
    graph = defaultdict(list)
    for land1, land2, cost in costs:
        graph[land1].append([cost, land2])
        graph[land2].append([cost, land1])
    
    max_list = []
    for i in range(n):
        max_list.append(dijkstra(i, graph, n))
    
    return max(max_list)

def dijkstra(start, graph, n):
    INF = sys.maxsize
    cost_list = [INF]*n
    heap = []

    cost_list[start] = 0
    heapq.heappush(heap, (cost_list[start], start))

    while heap:
        cur_cost, cur = heapq.heappop(heap)

        if cost_list[cur] < cur_cost:
            continue

        cost_list[cur] = cur_cost
        for adj_cost, adj in graph[cur]:
            new_cost = cur_cost + adj_cost
            if new_cost < cost_list[adj]:
                cost_list[adj] = new_cost
                heapq.heappush(heap, (cost_list[adj], adj))
    
    return max(cost_list)

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n, costs))
