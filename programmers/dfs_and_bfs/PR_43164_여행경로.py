from collections import defaultdict
import sys, heapq
sys.setrecursionlimit(10**6)

def solution(tickets):
    graph = defaultdict(list)

    for start, end in tickets:
        graph[start].append([end, 0])
    
    for value in graph.values():
        value.sort()
    
    return dfs(graph, tickets, 'ICN', ['ICN'])
    
def dfs(graph, tickets, start, route):
    if len(route) == len(tickets) + 1:
        return
    
    for idx, airport in enumerate(graph[start]):
        end = airport[0]
        flag = airport[1]

        if flag == 0:
            graph[start][idx][1] = 1
            route.append(end)
            dfs(graph, tickets, end, route)
            break

    return route

tickets = [["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]
print(solution(tickets))