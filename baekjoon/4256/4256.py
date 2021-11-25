import sys

def post_order(preorder, inorder):
    if len(preorder) == 0:
        return
    elif len(preorder) == 1:
        print(preorder[0], end=' ')
        return
    elif len(preorder) == 2:
        print(preorder[1], preorder[0], end=' ')
        return

    root = preorder[0]
    idx = inorder.index(root)
    # idx = 0
        
    # for i in range(len(inorder)):
    #     if inorder[i] == root:
    #         idx = i
    #         break

    post_order(preorder[1:idx+1], inorder[:idx])
    post_order(preorder[idx+1:], inorder[idx+1:])
    print(root, end = ' ')


if __name__=='__main__':
    input = sys.stdin.readline

    loop = int(input().strip())

    for _ in range(loop):
        n = int(input().strip())

        preorder = list(map(int, input().split()))
        inorder = list(map(int, input().split()))

        post_order(preorder, inorder)
        print()