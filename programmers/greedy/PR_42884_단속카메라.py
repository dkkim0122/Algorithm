from collections import deque

def solution(routes):
    routes = deque(sorted(routes))
    area = routes.popleft()
    result = []

    while routes:
        next = routes.popleft()
        # 겹치는 경우
        if next[0] <= area[1]:
            area = [next[0], area[1]]
            # 안에 포함되는 경우
            if next[1] < area[1]:
                area = [area[0], next[1]]
        else:
            result.append(area)
            area = next
        
    result.append(area)
    return len(result)

routes = [[1,10],[2,7],[3,5],[10,12]]
print(solution(routes))