import sys
 
input = sys.stdin.readline
 
n, k = map(int, input().split())
que = list(range(1, n + 1))
joseph_list = []
front = 0
no = n

while no > 0:
    if front % k == k-1:
        joseph_list.append(que[front])
        no -= 1
    else:
        que.append(que[front])

    front += 1

print('<', end='')
for i in range(n-1):
    print(f"{joseph_list[i]}, ", end='')

print(f'{joseph_list[n-1]}>')