def solution(N, number):
    
    dp = [[] for _ in range(8)]
    
    n = 1
    while (n < 8):
        if n == 1:
            dp[n] = [N]
            if N == number:
                return n
        
        for j in range(1, n):
            print(n, j, n-j)
            Cal(dp[n], dp[j], dp[n-j])
            dp[n] = list(set(dp[n]))
        if number in dp[n]:
            return n
        n += 1
        
    return -1


def cal(n, m):
    length = len(str(m))
    if m == 0:
        return [n*(10**length)+m, n+m, n-m, n*m]
    else:
        return [n*(10**length)+m, n+m, n-m, n*m, n//m]

def Cal(dp, dp1, dp2):
    for i in range(len(dp1)):
        for j in range(len(dp2)):
            dp.extend(cal(dp1[i], dp2[j]))

N = 5
number = 55

print(solution(N, number))