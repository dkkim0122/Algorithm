import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

def all_melt():
    for r in range(row):
        for c in range(col):
            if iceberg[r][c] !=0:
                return False
    return True

def check(iceberg, y, x): # 행이 y좌표 열이 x좌표
    num = 0
    for i in range(4): # 0:상, 1:우, 2:하, 3:좌
        new_r, new_c = y + dy[i], x + dx[i]
        if 0 <= new_r < row and 0 <= new_c < col \
            and iceberg[new_r][new_c] == 0:
            num += 1
        
    return num

def dfs(r,c):
    need_visit = deque([[r, c]])

    while need_visit:
        y, x = need_visit.popleft()
        for i in range(4):
            new_y, new_x = y+dy[i], x+dx[i]
            if 0<=new_x<col and 0<=new_y<row and visited_ice[new_y][new_x] != 0:
                visited_ice[new_y][new_x] = 0
                need_visit.append([new_y,new_x])
                

row, col = map(int, input().split())
iceberg = [[] for _ in range(row)]

for i in range(row):
    iceberg[i] = list(map(int, input().split()))

# print(iceberg)

dx = [0,1,0,-1] # 이런 테크닉 많이 쓰이는듯
dy = [1,0,-1,0]


year = 0


while True:
    year += 1
    if all_melt():
        print(0)
        break
    
    new_ice = deepcopy(iceberg) 
    # 빙산이 깎일 때, 기존의 빙산이랑 비교해야지, 
    # 지금 깎이고 있는 현재 빙산을 기준으로 삼으면 안 된다.

    # 각 좌표들에 대해 0 개수 세 주고 
    # print(new_ice)
    for r in range(row):
        for c in range(col):
            if iceberg[r][c] != 0:
                num = check(iceberg, r,c)
                if new_ice[r][c] - num <= 0:
                    new_ice[r][c] = 0
                else:
                    new_ice[r][c] -= num

    iceberg = new_ice # 다 깎였으면 업데이트

    visited_ice = deepcopy(iceberg)
    
    count = 0 # 빙산 요소의 크기

    # 이어져 있는 연결요소들의 개수를 구하기 위해 dfs 사용
    for r in range(row):
        for c in range(col):
            if visited_ice[r][c] != 0:
                visited_ice[r][c] = 0
                dfs(r,c)
                count += 1

    if count > 1:
        print(year)
        break


