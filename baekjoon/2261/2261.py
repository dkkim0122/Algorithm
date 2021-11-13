# 1) 양쪽 다 기준선 왼쪽에 있는 경우 
# 2) 기준선에 걸쳐 있는 경우 
# 3) 양쪽 다 기준선 오른쪽에 있는 경우 


import sys
input = sys.stdin.readline

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

# x축 기준 정렬
points.sort()


# 점 사이의 거리 계산
def dist(a: list, b: list) -> int:
    return (a[0]-b[0])**2 + (a[1]-b[1])**2


def get_min_dist(start: int, end: int) -> int:
   
    # 점이 하나밖에 없다면 의미가 없으므로 최댓값 계산
    # y축이 같아도 points 리스트에서는 서로 다른 인덱스에 있을 것이므로 상관 없다.
    if start == end:
        return sys.maxsize
    
    # 점이 두 개 남으면 이 두 점 사이의 거리 리턴
    if end-start == 1:
        return dist(points[start], points[end])
    
    # 기준선에 대한 분할정복 실행, 1) 3) 경우에 대한 최소 거리 구함
    mid = (start + end) // 2
    min_dist = min(get_min_dist(start, mid), get_min_dist(mid, end))


    # x축 기준으로 후보군 탐색
    target_points = []
    for i in range(start, end+1): # 전체 범위에 대해
        if (points[i][0] - points[mid][0]) ** 2 < min_dist: # 기준선과의 x방향 거리가 min보다 작으면
            target_points.append(points[i])

    # 후보군 y축 기준 정렬
    target_points.sort(key = lambda x: x[1]) # 인자 x에 대해 x[1]을 리턴해준다. 그 리턴값이 key.

    # y축 기준 후보군들 거리 비교
    # 가장 가까운 점으로부터 y축으로 비교한다. 
    # y축 거리가 min보다 더 작으면 그 때 실제 거리를 min과 비교한다.
    tar_len = len(target_points)
    for i in range(tar_len - 1):    # 기준이 되는 점
        for j in range(i + 1, tar_len): # 그 점 바로 다음 점부터
            if (target_points[i][1] - target_points[j][1]) ** 2 < min_dist:  # 먼저 y축부터 비교해주고
                min_dist = min(min_dist, dist(target_points[i], target_points[j])) # 작으면 실제 거리
            else:   # 만약 y축 거리가 넘어버리면
                break # 바로 다음 기준점으로
    
    return min_dist

print(get_min_dist(0, n-1))
