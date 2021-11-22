import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

def bfs(r, c):
    need_visit = deque([[r,c]])

    while need_visit and not (r==row-1 and c==col-1):
        y, x = need_visit.popleft()
        visited[y][x] = 1

        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]

            if 0<=new_x<col and 0<=new_y<row and maze[new_y][new_x] != 0 \
                and visited[new_y][new_x] == 0:
                need_visit.append([new_y, new_x])


row, col = map(int, input().split())
maze = [[] for _ in range(row)]

for i in range(row): 
    str = input().strip()
    for j in str:
        maze[i].append(int(j))

dx = [0,1,0,-1] # 상,우,하,좌
dy = [1,0,-1,0]
visited = [[0]*col for _ in range(row)]

bfs(0,0)
total = 0
for i in range(row):
    total += sum(visited[i])

print(total)