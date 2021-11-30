import sys
input = sys.stdin.readline

def find_max_path():

    dp[0] = stair_cost[0]
    dp[1] = max(0, dp[0]) + stair_cost[1]
    dp[2] = max(stair_cost[0], stair_cost[1]) + stair_cost[2]
    for i in range(3, N):
        dp[i] = max(dp[i-3] + stair_cost[i-1], dp[i-2]) + stair_cost[i]

    print(dp[N-1])


if __name__=='__main__':
    N = int(input().strip())
    stair_cost = [int(input().strip()) for _ in range(N)]

    dp = [0 for _ in range(N)]

    find_max_path()