def solution(land):
    dp = [[0] * 4 for _ in range(len(land))]
    dp[0] = land[0]

    for i in range(1, len(dp)):
        for j in range(4):
            dp[i][j] = max(dp[i-1][:j] + dp[i-1][j+1:]) + land[i][j]

    return max(dp[-1])


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))