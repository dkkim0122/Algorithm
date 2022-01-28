from collections import defaultdict, deque

def solution(n, computers):

    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                graph[i].append(j)

    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            answer += 1
            bfs(graph, visited, i)

    return answer

def bfs(graph, visited, start):
    need_visited = deque([start])

    while need_visited:
        cur = need_visited.popleft()
        for adj in graph[cur]:
            if visited[adj] == 0:
                visited[adj] = 1
                need_visited.append(adj)


computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
n = 3
print(solution(n, computers))