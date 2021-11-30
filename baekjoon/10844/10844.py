import sys
input = sys.stdin.readline


if __name__=='__main__':
    N = int(input().strip())

    dp = [[0] * 10 for _ in range(N+1)]

    # dp[1][0] = 0이다.
    for i in range(1, 10):
        dp[1][i] = 1

    if N >= 2:
        for i in range(2, N+1):
            for j in range(10):
                if j == 0:
                    dp[i][j] = dp[i-1][1] % 1000000000
                elif j == 9:
                    dp[i][j] = dp[i-1][8] % 1000000000
                else:
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000
    
    print(sum(dp[N])%1000000000)