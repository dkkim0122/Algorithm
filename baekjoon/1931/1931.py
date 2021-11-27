# 얘를 왜 그리디 알고리즘으로 풀어야 하는가

import sys
input = sys.stdin.readline


if __name__=='__main__':
    n = int(input().strip())
    meetings = []
    
    for i in range(n):
        start, end = map(int, input().split())
        meetings.append([start, end])
    
    meetings.sort()
    meetings.sort(key=lambda x:x[1])

    count = 0
    end_time = 0
    for i in range(n):
        if meetings[i][0] >= end_time:
            end_time = meetings[i][1]
            count += 1

    print(count)