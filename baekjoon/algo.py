import sys
input = sys.stdin.readline

def find_lis():
    for i in range(N):
        for j in range(0,i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    
    print(max(dp))


if __name__=='__main__':
    N = int(input().strip())
    arr = list(map(int, input().split()))

    # dp[i] = i가 들어있는 LIS 중 가장 긴 LIS의 길이
    dp = [1]*N

    find_lis()