import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline


# 후위 순환 : start와 end는 인덱스
def postorder(start, end):
    if start > end:
        return
    
    # 루트 노드 찾기
    root = preorder_list[start]
    idx = start + 1

    # 서브 트리를 나누기 위해 루트 노드의 오른쪽 자식을 찾는다
    while idx <= end:
        if preorder_list[idx] > root:
            break
        idx += 1

    
    # postorder 출력하기
    postorder(start+1, idx-1) # 왼쪽 서브트리

    postorder(idx, end) # 오른쪽 서브트리

    print(root) # 루트


preorder_list = []

# 입력
while True:
    node = input().strip()
    if node =='':
        break
    preorder_list.append(int(node))


postorder(0, len(preorder_list)-1)