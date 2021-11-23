import sys
from collections import deque
from copy import deepcopy

def water():
    while next_water:
        cy, cx = next_water.popleft()
        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            if 0<=ny<r and 0<=nx<c and forest[ny][nx]=='.':
                new_forest[ny][nx] = '*'
    print(new_forest)

    return new_forest
                 

def move():
    next_place = []
    while next_move:
        cy, cx = next_water.popleft()
        forest[cy][cx] = '.'
        for i in range(4):
            ny, nx = cy+dy[i], cx+dx[i]
            if 0<=ny<r and 0<=nx<c and forest[ny][nx]!='X':
                if forest[ny][nx] =='*':
                    pass
                elif forest[ny][nx] == '.':
                    next_place.append([ny,nx])
                    forest[ny][nx] = 'S'

    return next_place


if __name__=='__main__':
    input = sys.stdin.readline

    dx = [0,1,0,-1] # 상,우,하,좌
    dy = [-1,0,1,0]
    r, c = map(int, input().split())

    forest = [[] for _ in range(r)]
    for i in range(r):
        string = input().split()
        forest[i] = list(string[0])

    

    next_water = deque()
    hedge = 0
    beaver = 0
    count = 0

    while True:
        for i in range(r):
            for j in range(c):
                if forest[i][j] == '*':
                    next_water.append([i,j])
                elif forest[i][j] == 'S':
                    hedge = [i,j]
                elif forest[i][j] == 'D':
                    beaver = [i,j]
        
        print(next_water)
        print(hedge)
        print(beaver)

        # 물이 들이닥친다
        new_forest = deepcopy(forest)
        forest = water()

        print('first wave')
        for i in forest:
            print(i)

        # 고슴도치가 움직인다
        next_move = deque([hedge])
        print(move)
        next_move.append(move())
        print('hedge moves')
        print(next_move)
        for i in forest:
            print(i)


        count += 1

        if hedge == beaver:
            print(count)
            break

