import sys

def find_min_mult():
    dp = [[0]*n for _ in range(n)]
    # dp행렬 만들기 (n*n이다. 자료에는 n+1*n+1로 되어있긴 하다.)

    for i in range(1, n): # i번째 대각선을 볼 것이다.
        for j in range(0, n-i): # i번째 대각선은 n-i행까지 간다.
            dp[j][j+i] = 2**31 # 최댓값 잡아주고(문제 조건)
            for k in range(j, j+i): # k는 시작점부터 끝점-1까지
                dp[j][j+i] = min(dp[j][j+i], 
                dp[j][k]+dp[k+1][j+i] + costs[j]*costs[k+1]*costs[j+i+1])
    for i in dp:
        print(i)
    return dp[0][n-1]

if __name__=='__main__':
    n = int(input().strip())
    INF = sys.maxsize
    costs = [0] * (n+1)  # P(n+1)까지 있으므로
    for i in range(n):  # 0부터 출발한다. dp[i][j]에서 i=0인 경우부터 보기 위해.
        r, c = map(int, input().split())
        costs[i] = r
        costs[i+1] = c

    print(find_min_mult())
