import heapq
import sys
input = sys.stdin.readline

n = int(input())
hq = [] # 배열을 이용한다.

# 자연수를 입력하면 배열에 값을 입력
# 0을 입력하면 가장 큰 값을 출력하고 그 값을 배열에서 제거
for i in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(hq, -x)  # max heap을 사용하기 위해!
    else:
        if hq:
            max = heapq.heappop(hq)
            print(-max)
        else:   # 비어 있으면
            print(0)