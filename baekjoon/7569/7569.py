import sys
from copy import deepcopy
from collections import deque

def all_ripe():
    for k in range(h):
        for j in range(n):
            for i in range(m):
                if box[k][j][i] == 0: 
                    return False
    return True

def bfs(z,y,x):
    dx = [0,0,-1,1,0,0] # 상,하,좌,우,업,다운
    dy = [-1,1,0,0,0,0]
    dz = [0,0,0,0,1,-1]
    need_visit = deque([[z,y,x]])

    while need_visit:
        cz, cy, cx = need_visit.popleft()
        for i in range(6):
            nz, ny, nx = cz+dz[i], cy+dy[i], cx+dx[i]
            if 0<=nz<h and 0<=ny<n and 0<=nx<m:
                if box[nz][ny][nx] == 0:
                    new_box[nz][ny][nx] = 1
                elif box[nz][ny][nx] == 1:
                    need_visit.append([nz, ny, nx])
    return new_box


if __name__=="__main__":
    m, n, h = map(int, input().split())
    box = [[[] for _ in range(n)] for _ in range(h)]

    # box 만들기
    for j in range(n):
        box[0][j] = (list(map(int, input().split())))
    for k in range(1, h):
        box[k] = box[0]

    new_box = deepcopy(box)
    for k in range(h):
        for j in range(n):
            for i in range(m):
                if box[k][j][i] == 1:
                    bfs(k,j,i)

    print(new_box)