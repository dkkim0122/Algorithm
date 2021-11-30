import sys
input = sys.stdin.readline

def find_max_path():

    for i in range(N):
        if i == 0:
            dp[i] = stair_cost[i]
        elif i == 1:
            dp[i] = max(0, stair_cost[i-1]) + stair_cost[i]
        elif i == 2:
            dp[i] = max(stair_cost[0], stair_cost[1]) + stair_cost[i]
        else:
            dp[i] = max(dp[i-3] + stair_cost[i-1], dp[i-2]) + stair_cost[i]

    print(dp[N-1])


if __name__=='__main__':
    N = int(input().strip())
    stair_cost = [int(input().strip()) for _ in range(N)]

    dp = [0 for _ in range(N)]

    find_max_path()