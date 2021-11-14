# '('은 push,  ')'은 pop이라 가정한다.
# 아무것도 없을 때 pop하면 'NO'를 출력한다.

import sys
input = sys.stdin.readline

def determine(a: list) -> str:
    n = len(a)
    stack = [None] * n
    ptr = 0

    for i in range(n):
        if a[i] == '(':
            stack[i] = 1
            ptr += 1
        elif a[i] == ')':
            ptr -= 1
            if ptr < 0:
                return 'NO'
    if ptr == 0:
        return 'YES'                
    else:
        return 'NO'

n = int(input().strip())
lst = [input().strip() for _ in range(n)]
yes_no = [None] * n


for i in range(n):
    yes_no[i] = determine(lst[i])

for i in range(n):
    print(yes_no[i])