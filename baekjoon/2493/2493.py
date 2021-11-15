# 타워 리스트의 맨 끝 원소부터 search를 시작한다.
# 순차적으로 뒤에서부터 검색하며 현재 타워보다 낮은 높이의 원소를 만나면 pop한다.
# 현재 타워보다 높거나 같은 원소를 만나면 그 원소의 인덱스+1(ptr)를 출력한다.
# 원소의 개수가 500,000개 이하인데 완전 탐색으로 풀 수 있을까?

import sys
input = sys.stdin.readline

n = int(input().strip())
towers = list(map(int, input().split()))
result = [None] * n

for i in range(n - 1, -1, -1):
    ptr = i # 자기 자신 바로 앞 인덱스부터 시작
    
    while True:
        ptr -= 1
        if ptr < 0:
            result[i] = 0
            break
        elif towers[ptr] >= towers[i]:
            result[i] = ptr + 1  # 순서는 인덱스 + 1이므로
            break

for i in range(n):
    print(result[i], end=' ')