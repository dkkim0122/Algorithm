import sys
from collections import deque
input = sys.stdin.readline



if __name__=='__main__':
    row, col = map(int, input().split())
    used = [False]*4
    visited = [[[0,used]]*col for _ in range(row)]
 
    dx = [1,1,2,2]
    dy = [-2,2,-1,1]

    sick_knight = [row-1, 0]
    x = sick_knight[1]
    y = sick_knight[0]
    visited[y][x][0] = 1

    # if col<=4: # 이동 방법 상관 없음
    #     queue = deque()
    #     queue.append(sick_knight)
    #     while queue:
    #         cy, cx = queue.popleft()
    #         for i in range(4):
    #             nx = cx+dx[i]
    #             ny = cy+dy[i]
    #             if 0<=nx<col and 0<=ny<row and visited[ny][nx] == 0:
    #                 visited[ny][nx] = visited[cy][cx][0] + 1
    #                 queue.append([ny,nx])
    # else:
        
    queue = deque()
    queue.append([y,x])
    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0<=nx<col and 0<=ny<row and visited[ny][nx][0] == 0:
                visited[ny][nx][0] = visited[cy][cx][0] + 1
                visited[ny][nx][1][i] = True            
                queue.append([ny,nx])
    

    for i in visited:
        print(i)

