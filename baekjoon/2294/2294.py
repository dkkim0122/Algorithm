import sys
from collections import deque

def bfs():
    while need_visit:
        sum, count = need_visit.popleft()
        flags[sum] = 1
        for coin in coins:
            new_sum = coin + sum
            if new_sum <= target and flags[new_sum] == 0:
                flags[new_sum] = 1
                new_count = count + 1 # 다음 레벨이 된다. 만약 이 레벨에서 끝나면 count는 최솟값이 되겠지
                need_visit.append((new_sum, new_count))
                if new_sum == target:
                    return new_count
    return -1


if __name__=='__main__':
    input = sys.stdin.readline

    n, target = map(int, input().split())

    flags = [0]*(target+1) # 해당 숫자가 합산에 쓰였는지 알 수 있도록
    coins = []
    for i in range(n):
        coin = int(input().strip())
        if coin <= target:
            coins.append(coin)

    coins.sort(reverse=True)

    need_visit = deque()  # 합산된 값, 합산 횟수
    need_visit.append((0,0))
    print(bfs())