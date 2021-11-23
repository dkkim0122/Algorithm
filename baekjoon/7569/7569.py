import sys
from copy import deepcopy
from collections import deque

def bfs(z,y,x):
    dx = [0,0,-1,1,0,0] # 상,하,좌,우,업,다운
    dy = [-1,1,0,0,0,0]
    dz = [0,0,0,0,-1,1]
    need_visit = deque([[z,y,x]])
    visited = [[[0]*m for _ in range(n)] for _ in range(h)]
    visited[z][y][x] = 1

    while need_visit:
        cz, cy, cx = need_visit.popleft()
        for i in range(6):
            nz, ny, nx = cz+dz[i], cy+dy[i], cx+dx[i]
            if 0<=nz<h and 0<=ny<n and 0<=nx<m and visited[nz][ny][nx] == 0:
                visited[nz][ny][nx] = 1
                need_visit.append([nz, ny, nx])
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = box[cz][cy][cx] + 1 
                    # 각 토마토 자리에 익을때까지의 시간이 기록된다
    

if __name__=="__main__":
    input = sys.stdin.readline
    
    m, n, h = map(int, input().split())
    box = [[[] for _ in range(n)] for _ in range(h)]

    # box 만들기
    for k in range(h):
        for j in range(n):
            box[k][j] = (list(map(int, input().split())))

    # 익은 토마토에서부터 주변 토마토까지 탐색 시간
    for k in range(h):
        for j in range(n):
            for i in range(m):
                if box[k][j][i] == 1:
                    bfs(k,j,i)

    result = 0
    no_ripe = 0
    
    # 한번도 변하지 않은 애
    for k in range(h):
        for j in range(n):
            result = max(box[k][j])
            for i in range(m):
                if box[k][j][i] == 0: 
                    no_ripe = -1
                    break
    
    if no_ripe == -1:
        print(-1)
    else:
        if result == 1:
            print(0)
        else:
            print(result)
