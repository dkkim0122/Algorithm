import sys
input = sys.stdin.readline

if __name__=='__main__':
    N = int(input().strip())

    dp = [0] * (N+1)

    # dp[1]의 값은 0이므로 2부터 for문을 시작한다.
    # 숫자로 나누는 것이 -1하는 것보다 더 빨리 1로 도달할 것이다.
    # 따라서 맨 처음에 1을 뺀 값으로 dp[i]의 값을 업데이트 해 주고, 
    # 차례대로 3, 2로 나누며 dp[i]의 값을 더 작은 값으로 변경해간다.
    # 2와 3의 자리는 바뀔 수 있어도 -1을 하는 구문의 자리는 바뀔 수 없다.
    for i in range(2,N+1):
        dp[i] = dp[i-1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)

        
    print(dp)