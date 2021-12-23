import sys

def solution(n, times):
    MAX = sys.maxsize
    
    # mid : 총 걸린 시간.
    start = 1
    end = MAX
    answer = 0
    
    while start <= end:
        count = 0
        mid = (start + end) // 2
        for time in times:
            count += mid // time

        if count < n:
            start = mid + 1
        elif count >= n:
            if count == n:
                return mid
            else:
                end = mid - 1

    return answer

print(solution(6, [7,10]))