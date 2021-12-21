import heapq

def solution(jobs):
    heap = []
    for job in jobs:
        heapq.heappush(heap, [job[1], job[0]])
    
    total = heap[0][1]
    avg = 0

    while heap:
        total += heap[0][0]
        pop = heapq.heappop(heap)
        time = total - pop[1]
        avg += time  
        print(pop, total, time)
    
    return avg // len(jobs)