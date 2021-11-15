import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(input().strip())
stack = []
count = k

for i in range(n):
    while stack and count > 0:
        if num[i] > stack[-1]:
            stack.pop()
            count -= 1
        else:
            break

    stack.append(num[i])


# 마지막에 가장 큰 수들이 같은 값으로 여러 개 있는 경우
# 뒤의 수들로 겹치는 수들을 없애지 못해 잘못된 값이 나온다.
for i in range(n-k):
    print(stack[i], end='')