import sys
from collections import deque
from copy import deepcopy

def water():
    while next_water:
        cy, cx = next_water.popleft()
        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            if 0<=ny<r and 0<=nx<c and water_move[ny][nx]==INF:
                if ny != beaver_y and nx != beaver_x:
                    water_move[ny][nx] = water_move[cy][cx] + 1
                    next_water.append([ny, nx])

def move(start):
    start_y ,start_x = start
    next_place = deque([[start_y ,start_x]])

    while next_place:
        cy, cx = next_place.popleft()
        
        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            if 0<=ny<r and 0<=nx<c and hedge_move[ny][nx] == 0:
                if hedge_move[cy][cx] + 1 < water_move[ny][nx]:
                    hedge_move[ny][nx] = hedge_move[cy][cx] + 1
                    next_place.append([ny, nx])


if __name__=='__main__':
    input = sys.stdin.readline

    dx = [0,1,0,-1] # 상,우,하,좌
    dy = [-1,0,1,0]
    INF = sys.maxsize
    r, c = map(int, input().split())

    forest = [[] for _ in range(r)]
    for i in range(r):
        string = input().split()
        forest[i] = list(string[0])

    water_move = [[INF]*c for i in range(r)]
    hedge_move = [[0]*c for i in range(r)]

    next_water = deque()
    hedge_start = [0,0]
    beaver = [0,0]

    for i in range(r):
        for j in range(c):
            if forest[i][j] == '*':
                water_move[i][j] = 1
                next_water.append([i,j])
            elif forest[i][j] == 'S':
                hedge_move[i][j] = 1
                hedge_start = [i,j]
            elif forest[i][j] == 'D':
                beaver = [i,j] # 비버 집이 여기 있다
            elif forest[i][j] == 'X':
                water_move[i][j] = -1 # -1로 하면 나중에 고슴도치도 피해간다

    beaver_y = beaver[0]
    beaver_x = beaver[1]
    # print(beaver)

    water()
    # print(water_move)   

    move(hedge_start)
    # print(hedge_move)
    # print(f'water move = {water_move}') 
    # print(f'hedge_move = {hedge_move}')


    # max_time = 0
    # for row in hedge_move:
    #     for point in row:
    #         max_time = max(max_time, point)

    hedge_end = hedge_move[beaver_y][beaver_x]
    if  hedge_end != INF: # 비버 집에 잘 도착했다
        print(hedge_end-1)
    else:
        print('KAKTUS')


