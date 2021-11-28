import sys
input = sys.stdin.readline

def find_min_jump(N: int, small_rocks: list) -> int:
    INF = sys.maxsize
    max_speed = int((N*2)**0.5)
    dp = [[INF]*(max_speed+2) for _ in range(N+1)] # 속도(열)는 max_speed까지만 찾아보면 된다. 
    dp[1][0] = 0  # 1번 돌에 0의 속도로 도착하는 최소 횟수 0 : 처음 시작 지점

    # 갈 수 있는(small_rocks에 없는) 각 돌들에 대해서 도착 속도를 볼 것.
    for i in range(1, N+1):
        if i not in small_rocks:
            for j in range(1, int((i*2)**0.5)+1):  # i번째 돌에서 가질 수 있는 최대 속도.
                dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1
    
    result = min(dp[N])

    if result != INF:
        return result
    else:
        return -1
            


if __name__=='__main__':
    N, M = map(int, input().split())

    small_rocks = []
    for i in range(M):
        small_rocks.append(int(input().strip()))
    
    print(find_min_jump(N, small_rocks))