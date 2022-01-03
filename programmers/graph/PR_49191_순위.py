from collections import defaultdict

def solution(n, results):
    win = defaultdict(list)  # 해당 노드가 이긴 노드
    lose = defaultdict(list)  # 해당 노드가 진 노드

    for winner, loser in results:
        win[winner].append(loser)
        lose[loser].append(winner)
    
    for i in range(1, n+1):
        for loser in win[i]:
            win[i].extend(win[loser])
            win[i] = list(set(win[i]))
    for i in range(1, n+1):            
        for winner in lose[i]:
            lose[i].extend(lose[winner])
            lose[i] = list(set(lose[i]))

    count = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            count += 1

    return count





n = 5
results = [[1, 2], [4, 5], [3, 4], [2, 3]]
print(solution(n, results))
