import sys
input = sys.stdin.readline


if __name__=='__main__':
    n = int(input().strip())
    arr = list(map(int, input().split()))

    # dp[i] : i번째 원소가 들어갔을 때 만들 수 있는 LIS 길이
    dp = [1] * n 

    # 만약 나(arr[i])보다 내 앞의 값(arr[j])이 작다면,
    # j로 만들 수 있는 LIS(dp[j])보다 내가 1 더 클 것이다.
    # 이를 0부터 i-1까지 계속 탐색하면서 최대의 값을 찾으면 된다.
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]: 
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))
