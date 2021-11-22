import sys

n, m = map(int, input().split())

max_list = [[] for _ in range(n+1)]
min_list = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    min_list[a].append(b)
    max_list[b].append(a)


count = 0
for i in range(1, n+1):
    for max in max_list[i]:
        for num in max_list[max]:
            if num not in max_list[i]:
                max_list[i].append(num)
    if len(max_list[i]) >= n/2:
        count += 1

for i in range(1, n+1):
    for min in min_list[i]:
        for num in min_list[min]:
            if num not in min_list[i]:
                min_list[i].append(num)
    if len(min_list[i]) >= n/2:
        count += 1


print(count)
