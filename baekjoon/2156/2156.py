import sys
input = sys.stdin.readline

def drink_most_wine():
    for i in range(wine_num):
        if i == 0:
            dp[i] = wines[i]
        elif i == 1:
            dp[i] = wines[i] + wines[i-1]
        elif i == 2:
            dp[i] = max(wines[i-1] + wines[i], wines[i-2] + wines[i], dp[i-1])
        else:
            dp[i] = max(dp[i-3] + wines[i-1] + wines[i], 
                        dp[i-2] + wines[i],
                        dp[i-1])
    
    return dp[wine_num-1]


if __name__=='__main__':
    wine_num = int(input().strip())
    wines = [int(input().strip()) for _ in range(wine_num)]

    dp = [0] * wine_num

    print(drink_most_wine())