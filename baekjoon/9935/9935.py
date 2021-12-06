import sys
from collections import deque 
input = sys.stdin.readline

string = list(input().strip())
bomb = list(input().strip())
bomb_len = len(bomb)

stack= []

for i in range(len(string)):
    stack.append(string[i]) # 각 문자 stack에 넣기
    if len(stack) >= bomb_len: # stack에 들어있는 글자 수가 적어도 폭탄 길이보단 크거나 같아야.
        if stack[-bomb_len:] == bomb:
            for i in range(bomb_len):
                stack.pop()

if not stack:
    print('FRULA')
else:
    for i in range(len(stack)):
        print(stack[i],end='')
