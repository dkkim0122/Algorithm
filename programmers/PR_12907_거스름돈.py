def solution(n, money):
    dp = [0] * (n+1)

    for coin in money:
        dp[coin] += 1
        for price in range(coin, n+1):
            if coin <= price:
                dp[price] += dp[price-coin]
    return dp

print(solution(5, [2,3]))