import sys
input = sys.stdin.readline

n = int(input().strip())
heights = [None] * n
ptr = 0
max_height = 0
count = 0

for i in range(n):
    heights[i] = int(input().strip())
    ptr += 1

for i in range(n-1, -1, -1):
    if heights[i] > max_height:
        max_height = heights[i]
        count += 1

print(count)
