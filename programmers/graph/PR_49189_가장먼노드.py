from collections import defaultdict, deque

def solution(n, edge):
    graph = defaultdict(list)
    for node1, node2 in edge:
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    visited = [-1] * (n+1)

    def bfs(start):
        need_visit = deque([])
        need_visit.append([start, 0])
        visited[start] = 0

        while need_visit:
            node, cnt = need_visit.popleft()

            for adj in graph[node]:
                if visited[adj] == -1:
                    need_visit.append([adj, cnt+1])
                    visited[adj] = cnt + 1

    bfs(1)
    farthest = max(visited)

    return visited.count(farthest)

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, edge))