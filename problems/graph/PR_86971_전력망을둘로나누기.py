from collections import defaultdict
import sys

def solution(n, wires):
    answer = sys.maxsize

    for j in range(len(wires)):
        graph = make_graph(wires[:j]+wires[j+1:])
        visited = [False] * (n+1)
        result = []
        for i in range(1, n+1):
            if visited[i] == False:
                visited[i] = True
                result.append(check_number(i, graph, visited))

        answer = min(answer, abs(result[0] - result[1]))

    return answer

def make_graph(wires):
    graph = defaultdict(list)
    for node1, node2 in wires:
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph

def check_number(start, graph, visited):
    count = 1
    need_visit = [start]

    while need_visit:
        node = need_visit.pop()
        for adj in graph[node]:
            if visited[adj] == False:
                visited[adj] = True
                count += 1
                need_visit.append(adj)
    
    return count
    

print(solution(4, [[1,2],[2,3],[3,4]]))