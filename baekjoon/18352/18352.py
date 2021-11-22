import sys
import heapq

def dijkstra(graph, start):
    INF = sys.maxsize
    dist = [INF for _ in range(num_node+1)]
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (dist[start], start))

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)

        if dist[cur_node] < cur_dist:
            continue

        for adj in graph[cur_node]:
            new_dist = cur_dist + 1 # 1: cur_node와 adj_node까지의 거리는 1이므로
            if new_dist < dist[adj]:
                dist[adj] = new_dist
                heapq.heappush(queue, (dist[adj], adj))

    return dist


if __name__=='__main__':
    input = sys.stdin.readline

    num_node, num_edge, tar_dist, start = map(int, input().split())
    graph = [[] for _ in range(num_node+1)]

    for i in range(num_edge):
        come, to = map(int, input().split())
        graph[come].append(to)

    short_dist = dijkstra(graph, start)
    
    count = 0
    for i in range(1, num_node+1):
        if short_dist[i] == tar_dist:
            print(i)
            count += 1

    if count == 0:
        print(-1)


