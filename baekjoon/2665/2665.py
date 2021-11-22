import sys
import heapq


# 비용 문제와 같다고 할 수 있다.
def dijkstra(y, x):
    visited[y][x] = 1
    heap = []  # cost(검은 방을 만나서 바꾸는 횟수)
    heapq.heappush(heap, [0, y, x]) # (cost, y좌표, x좌표)
    cost_max = sys.maxsize
    
    while heap:
        cost, cy, cx = heapq.heappop(heap)

        if cy == n-1 and cx == n-1:
            return cost

        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if maze[ny][nx] == 0: # 벽을 만나면
                    heapq.heappush(heap, [cost+1, ny, nx])    
                else:
                    heapq.heappush(heap, [cost, ny, nx])


if __name__=='__main__':
    input = sys.stdin.readline

    n = int(input())
    maze = [[] for _ in range(n)]
    visited = [[0]*n for _ in range(n)]


    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(n):
        string = input().split()
        for j in range(n):
            maze[i].append(int(string[0][j]))


    print(dijkstra(0,0))
