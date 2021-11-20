import sys
input = sys.stdin.readline


# path compression
def find_root(node):
    if parent[node] != node: # 내가 루트가 아니면
        parent[node] = find_root(parent[node]) # 루트의 값을 찾아준다.
    return parent[node]

def union(node1, node2):
    root1 = parent[node1]
    root2 = parent[node2]

    # 루트들의 랭크 비교하기
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = []

    # 노드를 만들어준다.
    for node in nodes:
        make_set(node)
    
    # 가중치 기반으로 edge(경로)들을 sorting
    edges.sort()

    # 간선들을 연결한다.
    for edge in edges:
        weight, node1, node2 = edge
        # 두 노드가 사이클이 되는지를 체크
        if find_root(node1) != find_root(node2):
            union(node1, node2)
            mst.append(edge)

    # mst의 모든 weight값을 더한다.
    sum = 0
    for i in range(len(mst)):
        sum += mst[i][0]

    return sum

edges = []
nodes = []
parent = {}
rank = {}

num_ver, num_edge = map(int, input().split())

# 버텍스 리스트 만듦
nodes = [i+1 for i in range(num_ver)]

# 에지 리스트 만듦
for i in range(num_edge):
    node1, node2, weight = map(int, input().split())
    edges.append([weight, node1, node2])


print(kruskal(edges))