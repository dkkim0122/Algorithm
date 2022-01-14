from collections import deque

def solution(routes):
    routes = deque(sorted(routes))
    area = routes.popleft()
    count = 1

    while routes:
        next = routes.popleft()
        if next[0] <= area[1]: # 겹치는 경우
            area = [next[0], area[1]]
            if next[1] < area[1]: # 안에 포함되는 경우
                area = [area[0], next[1]]
        else:  # 겹치는 거 끝
            count += 1
            area = next
        
    return count

routes = [[1,10],[2,7],[3,5],[10,12]]
print(solution(routes))