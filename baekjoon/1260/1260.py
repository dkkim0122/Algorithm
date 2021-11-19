import collections
import sys
from collections import deque

input = sys.stdin.readline

def dfs_recur(edges, start_node, visited = []):
    visited.append(start_node)

    for node in edges[start_node]:
        if node not in visited:
            dfs_recur(edges, node, visited)

    return visited

def bfs(edges, start_node):
    visited = []
    need_visited = deque()
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.popleft()
        if node not in visited:
            visited.append(node)
            need_visited.extend(edges[node])
    
    return visited


node_num, edge_num, start_node = map(int, input().split())
# edges = {}

# for i in range(edge_num):
#     node1, node2 = map(int, input().split())
#     if node1 not in edges:
#         edges[node1] = [node2]
#     else:
#         edges[node1].append(node2)
    
#     if node2 not in edges:
#         edges[node2] = [node1]
#     else:
#         edges[node2].append(node1)
    
edges = collections.defaultdict(list)  # 딕셔너리의 기본값을 list로 초기화시켜준다.

for i in range(edge_num):
    node1, node2 = map(int, input().split())
    edges[node1].append(node2)
    edges[node2].append(node1)

edges.sort()

dfs_list = dfs_recur(edges, start_node, [])
bfs_list = bfs(edges, start_node)

for node in dfs_list:
    print(node, end=' ')
print()
for node in bfs_list:
    print(node, end=' ')