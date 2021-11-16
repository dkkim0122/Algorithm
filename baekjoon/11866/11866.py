import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
que = deque(range(1,n+1))
joseph_list = []
count = 0   # 인덱스의 개념이 아니다

while que:
    count += 1
    if count % k == 0:
        x = que.popleft()
        joseph_list.append(x)
    else:
        x = que.popleft()
        que.append(x)
    print(que, count)

print('<', end='')
for i in range(n-1):
    print(f"{joseph_list[i]}, ", end='')

print(f'{joseph_list[n-1]}>')
