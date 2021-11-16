import heapq
import sys

input = sys.stdin.readline

n = int(input().strip())
line_list = []
for _ in range(n):
    line = list(map(int, input().split()))
    line_list.append(line)

d = int(input())

# 후보군을 뽑자
target_line = []  # 후보군 라인

for line in line_list:
    start, end = line
    if abs(start - end) <= d:   # 길이가 기준보다 작은 애들만
        line = sorted(line)   # 시작점과 끝점을 정렬한다.
        target_line.append(line)

target_line.sort(key= lambda x:x[1])  # 끝점을 기준으로 오름차순으로 정렬한다.

# 가능한 실제 선분들을 뽑자
possible_line = []
ans = 0

for line in target_line:
    if not possible_line:   # 힙이 비어있으면 일단 해당 후보군을 넣자(어차피 가능한 친구다)
        heapq.heappush(possible_line, line)
    else:
        while possible_line[0][0] < line[1] - d: 
            heapq.heappop(possible_line)
            if not possible_line:
                break
        heapq.heappush(possible_line, line)
    ans = max(ans, len(possible_line))

print(ans)
