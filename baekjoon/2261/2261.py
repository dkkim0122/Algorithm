import sys


def dist(a: list, b: list) -> int:
    d = (a[0]-b[0])**2 + (a[1]-b[1])**2
    return int(d)

def min_dist(points: list, start: int, end: int) -> int:
   
    # start가 end에 도달했다면
    if start == end:
        return sys.maxsize

    # 일단 minimum의 초기값 : 가장 먼 두 점 사이의 거리(x좌표상)
    minimum = dist(points[start], points[end])
    # 루프 돌면서 start 값과 나머지 점 거리 계산 후 min값 계산
    for i in range(start + 1, end + 1):
        i_dist = dist(points[start], points[i])
        if i_dist < minimum:
            minimum = i_dist

    minimum = min(minimum, min_dist(points, start + 1, end))

    return minimum

n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]

points.sort()

print(min_dist(points, 0, n-1))