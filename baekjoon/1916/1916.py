import sys
import heapq

def dijkstra(start):
    INF = sys.maxsize
    dist = [INF for _ in range(num_node+1)]
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (dist[start], start))
    while queue:
        cur_cost, cur_node = heapq.heappop(queue)

        if dist[cur_node] < cur_cost: # 지금 테이블에 있는 값보다 작으면 고려할 필요가 없다
            continue

        for adj in graph[cur_node]:  # graph -> (end, cost)
            new_cost = cur_cost + adj[1] # 현 노드까지의 최소 비용 + 현 노드에서 인접 노드까지의 비용

            if new_cost < dist[adj[0]]:
                dist[adj[0]] = new_cost
                heapq.heappush(queue, (new_cost, adj[0]))
    return dist


if __name__ == '__main__':
    input = sys.stdin.readline

    num_node = int(input().strip())
    num_edge = int(input().strip())

    graph = [[] for _ in range(num_node + 1)]

    for i in range(num_edge):
        start, end, cost = map(int, input().split())
        graph[start].append((end, cost))  # 그래프 해당 도시 인덱스 값 : (도착 도시, 비용)
    
    start, end = map(int, input().split())

    short_list = dijkstra(start)
    print(short_list[end])