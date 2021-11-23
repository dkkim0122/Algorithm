import sys
from collections import deque

def bsf(start, target):
    need_cal = deque([start])
    count = 0
    while need_cal:
        coin = need_cal.popleft()
        target -= coin
        count += 1
        if target == 0:
            result.append(count)
            return
        for another_coin in coins:
            if target - another_coin > 0:
                need_cal.append(another_coin)
            elif target - another_coin == 0:
                count += 1
                result.append(count)


if __name__=='__main__':
    input = sys.stdin.readline

    n, target = map(int, input().split())
    coins = [int(input().strip()) for _ in range(n)]
    coins.sort(reverse=True)

    result = []

    for coin in coins:
        if target - coin >= 0:
            bsf(coin, target)

    if result != []:
        print(min(result))
    else:
        print(-1)