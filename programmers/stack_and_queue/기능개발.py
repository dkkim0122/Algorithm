def solution(progresses, speeds):
    answer = []
    
    while progresses: # 기능이 하나도 남지 않을 때까지
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # 모든 기능이 다 나가고 마지막으로 while문을 돌 때를 대비하여
        # progresses == True라는 구문을 넣었다.
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0) # 해당되는 기능이 나가면 같이 나가야 한다.
            count += 1
        
        if count != 0:
            answer.append(count)
        
    return answer