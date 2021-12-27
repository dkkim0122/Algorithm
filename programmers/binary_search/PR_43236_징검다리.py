from collections import deque

def solution(distance, rocks, n):
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()

    between = [0] * (len(rocks)-1)
    for i in range(0, len(rocks)-1):
        between[i] = rocks[i+1] - rocks[i]

    start = 0
    end = rocks[-1]
    ans = 0
    
    # mid : 각 바위 사이의 거리의 최솟값. 해당 최솟값을 만족시키기 위해 돌들을 계속 뺄 것이다.
    # count : 해당 mid를 만족시키기 위해 빼야 하는 돌의 최솟값.
    while start <= end:
        count = 0  # 돌을 뺀 횟수
        mid = (start + end)//2
        queue = deque(between)

        while queue:
            dis = queue.popleft()
            # 만약 최솟값보다 크다면 그 거리는 볼 필요 없으므로 그냥 버린다.
            # 만약 맨 앞의 두 돌 사이의 거리가 최솟값보다 작다면 그 돌을 빼서 거리를 더 키워야 한다.
            if dis < mid:  
                try:
                    queue[0] += dis  # 그 바로 뒤의 거리에 더해준다(그 돌을 뺀다.)
                    count += 1  # 돌을 뺐으므로 + 1
                except: # 만약 마지막 거리가 최솟값보다 작으면 그 돌을 빼 준다.
                    count += 1
        
        
        if count <= n:  # 돌을 기준보다 덜 빼도 최솟값을 만들 수 있다면 
            ans = mid   # 괜찮긴 한데
            start = mid + 1   # 그래도 최솟값을 더 늘여보자. 
        elif count > n:  # 주어진 기준보다 돌을 더 많이 빼야 한다면 최솟값이 너무 큰 것이다. 
            end = mid - 1
    
    return ans