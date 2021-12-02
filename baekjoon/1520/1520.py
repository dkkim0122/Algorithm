# 메모이제이션?
# dp[i][j]의 값
# -INF : 방문하지 않은 값이므로 방문
# 0 : 목적지까지 갈 수 없는 값일 경우 0
# 1 이상 : 해당 좌표를 거쳐 끝점까지 갈 수 있는 경우의 수

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(y, x):
    if y == row-1 and x == col-1:
        return 1
    
    if dp[y][x] == -INF:
        dp[y][x] = 0
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=nx<col and 0<=ny<row and maps[y][x] > maps[ny][nx]:
                dp[y][x] += dfs(ny,nx)

    return dp[y][x]                


if __name__ == '__main__':
    INF = sys.maxsize
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    row, col= map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(row)]
    dp = [[-INF] * col for _ in range(row)]

    print(dfs(0,0))