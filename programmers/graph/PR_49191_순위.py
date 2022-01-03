from collections import defaultdict

def solution(n, results):
    win = defaultdict(set)  # 해당 노드가 이긴 노드
    lose = defaultdict(set)  # 해당 노드가 진 노드

    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)
    
    for i in range(n):
        for loser in win[i]:
            win[i] |= win[loser]
        for winner in lose[i]:
            lose[i] |= lose[winner]

    print(win)
    print(lose)


    answer = 0
    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
solution(n, results)
