import sys
input = sys.stdin.readline

def padovan(N):
    if N == 1 or N == 2 or N == 3:
        dp[N] = 1
        return 1
    
    if dp[N] != 0:
        return dp[N]
    
    dp[N] = padovan(N-2) + padovan(N-3)
    return dp[N]

if __name__=='__main__':
    test_num = int(input().strip())

    dp = [0]*101

    for _ in range(test_num):
        N = int(input().strip())

        print(padovan(N))
