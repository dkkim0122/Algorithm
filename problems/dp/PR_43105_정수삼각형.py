def solution(triangle):
    N = len(triangle)

    dp = [[0]*i for i in range(1, N+1)]

    n = 0
    while (n < N):
        if n == 0:
            dp[n][0] = triangle[n][0]

        for i in range(n+1):
            if i == 0:
                dp[n][0] = dp[n-1][0] + triangle[n][0]
            elif i == n:
                dp[n][n] = dp[n-1][n-1] + triangle[n][n]
            else:
                dp[n][i] = max(dp[n-1][i-1], dp[n-1][i]) + triangle[n][i]
        
        n += 1
    
    return max(dp[-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))