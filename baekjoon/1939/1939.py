import sys
from collections import defaultdict, deque

def find_limit(mid):
    visited = [False] * (node_num + 1)
    need_visit = deque()
    need_visit.append(start_isl)
    visited[start_isl] = True

    while need_visit:
        start = need_visit.popleft() # 모든 경로부터 불가능한 경로를 없애가야 하니까 BFS?
        if start == end_isl:
            return True
        for adj, weight in graph[start]:
            if not visited[adj] and weight >= mid:
                need_visit.append(adj)
                visited[adj] = True

    return False


if __name__ == '__main__':
    input = sys.stdin.readline

    node_num, bridge_num = map(int, input().split())
    graph = defaultdict(list)

    min_weight, max_weight = 1, 1000000000

    for i in range(bridge_num):
        node1, node2, weight = map(int, input().split())
        graph[node1].append([node2, weight])
        graph[node2].append([node1, weight])
        min_weight = min(weight, min_weight)
        max_weight = max(weight, max_weight)

    start_isl, end_isl = map(int, input().split())

    result = 0
    while min_weight <= max_weight:
        mid_weight = (min_weight + max_weight)//2
        
        if find_limit(mid_weight): # 만약 이 값으로 가능하다면 더 올려도 된다.
            result = mid_weight
            min_weight = mid_weight + 1
        else:
            max_weight = mid_weight - 1

    print(result)