from collections import defaultdict, deque

def solution(n, results):
    win = defaultdict(set)  # 해당 노드가 이긴 노드
    lose = defaultdict(set)  # 해당 노드가 진 노드

    for winner, loser in results:
        win[winner].add(loser)  
        lose[loser].add(winner)

    for i in range(1, n+1):
        for loser in win[i]:  # i에게 진 애들 : loser
            lose[loser].update(lose[i])  # i를 이긴 애들은 역시 loser를 이겼다.
        for winner in lose[i]: # i를 이긴 애들
            win[winner].update(win[i])  # i한테 진 애들은 winner한테도 졌다.

    count = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            count += 1

    return count


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))
