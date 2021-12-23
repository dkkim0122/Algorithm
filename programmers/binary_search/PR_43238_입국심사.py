def solution(n, times):
    # mid : 총 걸린 시간.
    start = min(times)
    end = n * max(times)
    answer = 0
    
    while start <= end:
        count = 0
        mid = (start + end) // 2
        for time in times:
            count += mid // time

        if count < n:
            start = mid + 1
        elif count >= n:
            answer = mid
            end = mid - 1

    return answer
