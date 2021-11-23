import sys
from collections import deque

# 물의 경로
def water():
    while next_water:
        cy, cx = next_water.popleft()
        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            # 물이 갈 수 있는 길
            if 0<=ny<r and 0<=nx<c and forest[ny][nx] == '.' and water_move[ny][nx]==-1: 
                water_move[ny][nx] = water_move[cy][cx] + 1 # 각 위치에 물이 차는 시간을 저장한다
                next_water.append([ny, nx])

# 고슴도치의 경로
def move(start):
    start_y ,start_x = start
    next_place = deque([[start_y ,start_x]])

    while next_place:
        cy, cx = next_place.popleft()
        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            # 고슴도치가 갈 수 있는 경로('.'과 'D'는 갈 수 있다)
            if 0<=ny<r and 0<=nx<c and forest[ny][nx] in '.D' and hedge_move[ny][nx] == -1:
                # 1.한 시간 뒤보다 더 늦게 물이 들어오면 || 2.물이 안 들어온 애들이면 고슴도치가 갈 수 있다
                if hedge_move[cy][cx] + 1 < water_move[ny][nx] or water_move[ny][nx] == -1:
                    hedge_move[ny][nx] = hedge_move[cy][cx] + 1
                    next_place.append([ny, nx])


if __name__=='__main__':
    input = sys.stdin.readline

    dx = [0,1,0,-1] # 상,우,하,좌
    dy = [-1,0,1,0]
    r, c = map(int, input().split())

    forest = [[] for _ in range(r)]
    for i in range(r):
        string = input().split()
        forest[i] = list(string[0])

    water_move = [[-1]*c for i in range(r)]  # default 값은 -1로 해준다.
    hedge_move = [[-1]*c for i in range(r)]

    next_water = deque()
    hedge_start = [0,0]
    beaver = [0,0]

    for i in range(r):
        for j in range(c):
            if forest[i][j] == '*':
                water_move[i][j] = 0 # 0부터 시작
                next_water.append([i,j])
            elif forest[i][j] == 'S':
                hedge_move[i][j] = 0 # 0부터 시작
                hedge_start = [i,j]
            elif forest[i][j] == 'D':
                beaver = [i,j] # 비버 집이 여기 있다

    # 비버 집 좌표
    beaver_y = beaver[0]
    beaver_x = beaver[1]

    water() # 물이 흐르고
    move(hedge_start) # 고슴도치가 이동

    hedge_end = hedge_move[beaver_y][beaver_x]
    if  hedge_end != -1 : # 비버 집에 잘 도착했다
        print(hedge_end)
    else:
        print('KAKTUS')