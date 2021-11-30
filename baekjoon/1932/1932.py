import sys
input = sys.stdin.readline

def find_max_path():
    
    for i in range(n):
        if i == 0:
            dp[i] = triangle[0]
            continue

        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][i-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    return max(dp[n-1])


if __name__ == '__main__':
    n = int(input().strip())

    triangle = [list(map(int, input().split())) for _ in range(n)]

    dp = [[-1] * i for i in range(1, n+1)]

    print(find_max_path())