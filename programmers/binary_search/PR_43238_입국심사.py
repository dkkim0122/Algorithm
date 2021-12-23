import sys

def solution(n, times):
    MAX = sys.maxsize
    
    lst = []
    
    start = 0
    end = MAX
    ret = MAX
    
    while start <= end:
        count = 0
        mid = (start + end) // 2
        for time in times:
            if mid % time == 0:
                count += mid // time
        if count == n:
            return mid
        elif count < n:
            end = mid - 1
        else:
            start = mid + 1

print(solution(6, [7,10]))