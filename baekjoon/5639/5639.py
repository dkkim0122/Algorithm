import sys
input = sys.stdin.readline

# 후위 순환
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root)

nodes = []
tree = {}

# 입력
while True:
    node = input().strip()
    if node =='':
        break
    nodes.append(int(node))

# 트리를 만들어라
tree[nodes[0]] = ['.','.']

for i in range(1, len(nodes)):
    tree[nodes[i]] = ['.','.']
    if nodes[i] < nodes[i-1]:
        tree[nodes[i-1]][0] = nodes[i]
    else:
        j = i-2
        while nodes[i] > nodes[j]:
            if j == -1: # 루트 노드의 오른쪽 값을 위해
                break
            j -= 1
        tree[nodes[j+1]][1] = nodes[i]

postorder(nodes[0])