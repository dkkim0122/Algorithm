import sys
input = sys.stdin.readline


m, n, l = map(int, input().split())
shooters = list(map(int, input().split()))
shooters.sort()

animals = []
for i in range(n):
    x, y = map(int, input().split())
    if y <= l:  # 먼저 y축이 너무 먼 동물들을 제외시킨다.
        animals.append([x, y])
animals.sort()

count = 0

for i in range(len(animals)):
    start = 0
    end = len(shooters)-1 # 사대에 대해 탐색을 수행
    
    while start <= end:
        mid = (start+end)//2
        if abs(shooters[mid]-animals[i][0]) + animals[i][1] <= l: #조건에 맞으면 다음 동물로.
            count += 1
            break
        else:
            if shooters[mid] <= animals[i][0]:
                start = mid + 1
            else:
                end = mid - 1

print(count)
