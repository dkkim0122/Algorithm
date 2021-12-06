# 점화식을 세우는 것이 중요하겠다.
# target 값보다 작은 값에서 경우의 수를 더해간다는 발상은 좋았는데,
# 주어진 동전의 값을 작은 것부터 먼저 경우의 수를 산출한다는 생각은 하지 못했다.
# 거꾸로 해도 답은 나온다. 당연히.

import sys
input = sys.stdin.readline

def find_num(coin_list, target_number):
    dp = [0]*(target_number+1)
    
    for coin in coin_list:
        if coin > target_number:  # coin이 target값보다 더 크면 안 된다.
            continue
        dp[coin] += 1  # 자기 자신 추가
        for i in range(coin, target_number+1): # 자기 자신보다 큰 것만 보면 된다.
            dp[i] = dp[i] + dp[i-coin] # 가장 작은 coin부터 쌓아올린 경우의 수 + 내가 더해짐으로서 얻을 수 있는 경우의 수
    
    return dp[target_number]

if __name__=='__main__':
    test_num = int(input().strip())

    for i in range(test_num):
        coin_num = int(input().strip())
        coins = list(map(int, input().split()))
        target = int(input().strip())

        print(find_num(coins, target))