# 숫자가 들어올 때마다 값들을 크기 순서대로 새로 정렬해주어야 한다.
# 정렬된 배열의 중간 값을 출력한다.



import heapq
import sys

input = sys.stdin.readline

n = int(input())
leftheap = []
rightheap = []

for i in range(n):
    add = int(input())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, (-add, add)) # 최소힙(중간값보다 작은 애들)에서는 최댓값대로
    else:
        heapq.heappush(rightheap, (add, add)) # 최대힙에서는 최솟값대로

    if rightheap and leftheap[0][1] > rightheap[0][1]:
        max = heapq.heappop(leftheap)[1]
        min = heapq.heappop(rightheap)[1]

        heapq.heappush(leftheap, (-min, min))
        heapq.heappush(rightheap, (max, max))

    print(leftheap[0][1])