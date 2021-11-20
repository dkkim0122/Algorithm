import sys
from collections import deque
import collections

input = sys.stdin.readline

def dfs(tree, start):
    need_visited = deque([start])

    while need_visited:
        node = need_visited.pop()
        for child in tree[node]:
            need_visited.append(child)
            if parents[child] == 0:
                parents[child] = node
            tree[child].remove(node)
            
    return parents


node_num = int(input())

tree = [[]*(node_num+1) for _ in range(node_num+1)]
parents = [0] * (node_num + 1)
parents[1] = 1


for i in range(node_num-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
dfs(tree, 1)

for parent in parents[2:]:
    print(parent)