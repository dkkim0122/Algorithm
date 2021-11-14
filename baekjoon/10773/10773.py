import sys
input = sys.stdin.readline


n = int(input().strip())

lst = [None] * n
ptr = 0
sum = 0

for i in range(n):
    num = int(input().strip())
    if num == 0:
        ptr -= 1
    else:
        lst[ptr] = num
        ptr += 1


for i in range(ptr):
    sum += lst[i]

print(sum)
