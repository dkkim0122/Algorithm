import sys
input = sys.stdin.readline

def padovan(N):
    if N == 1 or N == 2 or N == 3:
        dp[N] = 1
        return 1
    
    if N == 4 or N == 5:
        dp[N] = 2
        return 2
    
    if dp[N] != 0:
        return dp[N]
    
    dp[N] = padovan(N-1) + padovan(N-5)
    return dp[N]

if __name__=='__main__':
    test_num = int(input().strip())

    dp = [0]*101

    for _ in range(test_num):
        N = int(input().strip())

        print(padovan(N))
