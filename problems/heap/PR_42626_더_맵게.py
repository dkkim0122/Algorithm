import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville:
        if len(scoville) == 1 and scoville[0] < K:
            return -1

        food1 = heapq.heappop(scoville)
        if food1 >= K:
            return count

        food2 = heapq.heappop(scoville)
        heapq.heappush(scoville, food1 + 2*food2)
        count += 1
