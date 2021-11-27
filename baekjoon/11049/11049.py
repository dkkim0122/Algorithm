import sys

def find_min_mult():
    dp = [[INF]*(n+1) for _ in range(n+1)]
    # dp행렬 만들기
    for i in range(n+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif i == j:
                dp[i][j] = 0 # 대각선은 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i < j :
                lst = []
                for k in range(i, j): # k는 i부터 j-1까지
                    lst.append(dp[i][k]+dp[k+1][j] + costs[i]*costs[k+1]*costs[j+1])
                dp[i][j] = min(lst)
    
    return dp[1][n]

if __name__=='__main__':
    n = int(input().strip())
    INF = sys.maxsize
    costs = [0] * (n+2)  # P(n+1)까지 있으므로
    for i in range(1, n+1):
        r, c = map(int, input().split())
        costs[i] = r
        costs[i+1] = c

    print(find_min_mult())
