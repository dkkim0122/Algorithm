import sys
from collections import deque
import collections

input = sys.stdin.readline

def dfs(tree, start):
    visited = []
    need_visited = deque([start])

    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(tree[node])
            for child in tree[node]:
                if parent[child] == 0:
                    parent[child] = node

    return visited


tree = collections.defaultdict(list)
node_num = int(input())
parent = [0] * (node_num + 1)
parent[1] = 1


for i in range(node_num-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
dfs(tree, 1)

for parent_node in parent[2:]:
    print(parent_node)