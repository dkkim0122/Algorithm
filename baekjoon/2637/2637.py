# 위상 정렬로 어떻게 풀지..?
# dp로 어떻게 풀지..?

import sys

if __name__=='__main__':
    input = sys.stdin.readline

    node_num = int(input())
    edge_num = int(input())

    dp = [[] for _ in range(node_num+1)]
    lst = []

    for i in range(edge_num):
        lst.append(list(map(int,input().split())))

    lst.sort()
    # print(f'lst : {lst}')

    basic_parts = lst[0][0]-1
    for i in range(1,basic_parts+1):
        dp[i] = [i]
    # print(f'dp : {dp}')

    for i in range(edge_num):
        idx, parts, num = lst[i]
        for _ in range(num):
            dp[idx].extend(dp[parts])
        # print(f'idx: {idx} dp:{dp[idx]}')

    for i in range(1,basic_parts+1):
        print(f"{i} {dp[node_num].count(i)}")