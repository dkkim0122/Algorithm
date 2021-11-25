import sys
import heapq

def check(need_visit):
    while need_visit:
        val, cy, cx = heapq.heappop(need_visit)
    
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=nx<n and 0<=ny<n and test[ny][nx] == 0 and visited[ny][nx] == 0:
                test[ny][nx] = val
                next_need_visit.append([val, ny, nx])


if __name__=='__main__':
    input = sys.stdin.readline

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    n, virus_num = map(int, input().split())

    test = [[] for _ in range(n)]
    for i in range(n):
        test[i] = list(map(int, input().split()))

    sec, final_y, final_x = map(int, input().split())

    count = 0
    visited = [[0]*n for _ in range(n)]

    need_visit = [] # 우선순위 큐

    for i in range(n):
        for j in range(n):
            if test[i][j] != 0 and visited[i][j] == 0:
                visited[i][j] = 1
                heapq.heappush(need_visit, [test[i][j],i,j])
    
    while True:
        if count == sec:
            print(test[final_y-1][final_x-1])
            break
        next_need_visit = [] # 시간초과 막기 위해
        check(need_visit)

        need_visit = next_need_visit

        count += 1