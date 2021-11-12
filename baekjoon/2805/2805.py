
def bin_search(trees:list, key:int) -> int:
    n = len(trees)
    start = 1  # tree[0]가 아니라 가장 짧은 길이인 1로 두어야 한다.
    end = trees[n-1] # 가장 높은 tree
    result = 0

    while start <= end:
        h = (start + end) // 2

        wood = 0  # 벤 나무 총합
        for tree in trees: # 나무들에 대해 h 보다 크면 (나무 - h) 합산
            if tree > h:
                wood += tree - h

        # 만약 벤 나무들의 합이 key값과 딱 맞아 떨어지거나 크면 일단 만족하지만
        # 또 최댓값은 아닐 수 있으니 h 값을 올려서 탐색한다.
        if wood >= key:
            result = h
            start = h + 1
        # 합이 key보다 작으면 h가 너무 높은 것이다.
        else:
            end = h - 1

    # 다 계산을 진행했으면 result값을 리턴
    return result


n, key = map(int, input().split())

trees = list(map(int, input().split()))

trees.sort()

print(bin_search(trees, key))