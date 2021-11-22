import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

def bfs(r, c):
    need_visit = deque([[r,c]])
    visited[r][c] = 1

    while need_visit:
        y, x = need_visit.popleft()

        if y == row-1 and x == col-1:
            return visited[y][x]      

        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]

            if 0<=new_x<col and 0<=new_y<row and maze[new_y][new_x] != 0: # 길이 있다
                if visited[new_y][new_x] == 0: # 방문한 적 없다.
                    need_visit.append([new_y, new_x])
                    visited[new_y][new_x] = visited[y][x] + 1 # 이렇게 정의하면
                    # 갈 수 있는 가능성이 있는 길까지 걸린 칸의 개수
                

row, col = map(int, input().split())
maze = [[] for _ in range(row)]

for i in range(row): 
    str = input().strip()
    for j in str:
        maze[i].append(int(j))

dx = [0,1,0,-1] # 하,우,상,좌
dy = [1,0,-1,0]
visited = [[0]*col for _ in range(row)]

print(bfs(0,0))
