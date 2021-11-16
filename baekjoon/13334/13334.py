import sys
import heapq

def search(start, end):
    max_count = 0
    mid = (start + end) // 2

    pl = mid - d
    pr = mid + d
    print(f'mid = {mid}, pl : {pl}, pr = {pr}')

    if start == end:
        return 0

    for i in range(n):
        if points[i][0] >= pl and points[i][1] <= pr:
            max_count += 1

    max_count = max(max_count, search(start, mid), search(mid, end))

    print(f"max = {max_count}")

    return max_count

input = sys.stdin.readline

n = int(input())
points = []

for i in range(n):
    point = list(map(int, input().split()))
    if point[1] < point[0]:
        point = [point[1], point[0]]
    heapq.heappush(points, point)

print(points)

d = int(input())

print(search(points[0][0], points[-1][1]))