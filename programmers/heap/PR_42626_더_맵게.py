import heapq

def solution(scoville, K):
    heap = []
    for food in scoville:
        heapq.heappush(heap, food)
    
    count = 0
    while heap:
        if len(heap) == 1 and heap[0] < K:
            return -1

        food1 = heapq.heappop(heap)
        if food1 >= K:
            return count

        food2 = heapq.heappop(heap)
        heapq.heappush(heap, food1 + 2*food2)
        count += 1
