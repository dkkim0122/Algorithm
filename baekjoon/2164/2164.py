# 디큐와 디큐-인큐를 반복

import sys
input = sys.stdin.readline

n = int(input())

cards = [None] * 5000000

for i in range(n):
    cards[i] = i+1

front = 0
rear = n  # n개
no = rear
count = 0

while no > 1:
    if count % 2 == 0: # deque
        count += 1
        front += 1
        no -= 1

    else: # deque and enque
        count += 1
        # deque
        x = cards[front]
        front += 1
        no -= 1

        # enque
        cards[rear] = x
        rear += 1
        no += 1

print(cards[front])

