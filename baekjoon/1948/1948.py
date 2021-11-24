import sys
from collections import deque
from collections import defaultdict

def topology_sort():
    queue = deque()
    
    for i in range(1, city_num + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        start = queue.popleft()
        for adj, cost in graph[start]:
            indegree[adj] -= 1
            max_length[adj] = max(max_length[adj], max_length[start] + cost) # 최대 거리 갱신
            if indegree[adj] == 0:
                queue.append(adj)
                
    print(max_length[end_city])

    # back tracking
    queue = deque()
    queue.append(end_city)
    count = 0 # 최장 경로의 도로 수
    check = [0] * (city_num + 1) # 해당 도로를 조사하였는가?
    # idx: 인접 노드 중 출발노드 value: 도착 노드

    while queue:
        start = queue.popleft()
        for adj, cost in back_graph[start]:
            # 해당 도로가 최장 경로 안의 도로이다 
            if max_length[start] == max_length[adj] + cost: # 해당 도시가 경로 안에 있다
                count += 1 
                if check[adj] == 0: # 조사하지 않았으면 중복 방지
                    queue.append(adj)
                    check[adj] = 1
    
    print(count)


if __name__=='__main__':
    input = sys.stdin.readline

    city_num = int(input())
    road_num = int(input())

    graph = defaultdict(list)
    back_graph = defaultdict(list)
    indegree = [0] * (city_num + 1)
    max_length = [0] * (city_num + 1) # 출발점에서 해당 도시까지 가기 위한 최대 거리

    for i in range(road_num):
        start, end, cost = map(int, input().split())
        graph[start].append((end, cost))
        back_graph[end].append((start, cost))
        indegree[end] += 1
    
    start_city, end_city = map(int, input().split())

    topology_sort()