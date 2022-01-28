def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while progresses: # 기능이 하나도 남지 않을 때까지
        # 개발이 완료된 기능들을 빼거나
        # 완료된 기능이 없으면 지금까지 셌던 count를 append해준다.
        if (progresses[0] + speeds[0] * time) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    
    answer.append(count) # 맨 마지막 기능 빼 주기 위해
        
    return answer