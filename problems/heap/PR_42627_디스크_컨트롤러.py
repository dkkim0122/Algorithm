import heapq

def solution(jobs):
    heap = []
    finished_job = 0  # 끝난 작업의 개수
    time = 0  # 현재 시간
    start = -1  # 마지막 작업이 시작한 시간
    avg = 0  # 작업의 요청부터 종료까지 걸린 시간의 총합

    while finished_job < len(jobs):
        # 현재 시간에 작업할 수 있는 후보
        # 마지막 작업이 시작했을 때부터 지금까지
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(heap, [job[1], job[0]])
    
        if len(heap) > 0:
            doing = heapq.heappop(heap)
            start = time
            time += doing[0]  # 작업이 끝난 후의 시각
            avg += (time - doing[1])  # 작업 끝난 시각 - 호출된 시각
            finished_job += 1
        else:
            time += 1
    
    return avg // len(jobs)