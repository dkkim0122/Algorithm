# 타워 리스트의 맨 끝 원소부터 search를 시작한다.
# 순차적으로 뒤에서부터 검색하며 현재 타워보다 낮은 높이의 원소를 만나면 ptr-=1한다.
# 현재 타워보다 높거나 같은 원소를 만나면 그 원소의 순서(인덱스+1)를 출력한다.
# 원소의 개수가 500,000개 이하인데 완전 탐색으로 풀 수 있을까?

import sys
input = sys.stdin.readline

n = int(input().strip())
towers = list(map(int, input().split()))
stack = []  # [탑 위치, 높이] 가 저장된다.
result = [0] * n

for i in range(n):
    while stack:
            # stack의 맨 마지막 저장된 탑과 비교한다.
            if towers[i] > stack[-1][1]:   # 만약 새로 들어온 탑이 더 높다면
                stack.pop() # 기존 탑을 pop하고 계속 송신할 탑을 찾아나간다.
            else:
                result[i] = stack[-1][0]
                break   # 찾았으면 while문을 break한다.
    
    stack.append([i+1, towers[i]]) # 해당 탑을 stack에 push한다.

print(*result)