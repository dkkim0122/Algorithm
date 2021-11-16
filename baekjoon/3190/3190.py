import sys
from collections import deque

def is_dead(snake: deque) -> None:
    body = [snake[i] for i in range(len(snake)-1)]
    if len(snake) > 1 and snake[-1] in body:   # 자기 몸에 부딪힐 때
        return True
    elif 0 < snake[-1][0] < n and 0 <snake[-1][1] <n: # 구간 안에서 움직일 때
        return False 
    elif len(snake) == 1:
        return False
    else:
        return True

def move(snake: deque) -> None:
    x_head = snake[-1][0]
    y_head = snake[-1][1]

    if direction == 'up':
        snake.append([x_head, y_head + 1])
    elif direction == 'left':
        snake.append([x_head-1, y_head])
    elif direction == 'down':
        snake.append([x_head, y_head-1])
    else:
        snake.append([x_head + 1, y_head])

    if snake[-1] in apple:
        del apple[snake[-1]]
    else:
        snake.popleft()

def turn(direction, order: str):
    idx = 0
    for i in range(4):
        if direc[i] == direction:
            idx = i
    if order == 'L':
        direction = (idx-1)%4
    else:
        direction = (idx+1)%4
    return direction
        

input = sys.stdin.readline

snake = deque([[0,0]])  # 머리는 snake[-1]
direc = ['up', 'right', 'down', 'left']
# left면 direction[(i-1)%4]
# right면 direction[(i+1)%4]
direction = direc[1]
time = 0

n = int(input())

apple_n = int(input())
apple = [list(map(int, input().split())) for _ in range(apple_n)]

turn_n = int(input())
turns = {}
for i in range(turn_n):
    sec, order = input().split()
    sec = int(sec)
    turns[sec] = order

while not is_dead(snake):
    if time in turns.keys():
        direction = turn(direction, turns[time])
    move(snake)
    time += 1


print(time)

