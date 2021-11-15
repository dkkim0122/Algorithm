from typing import Any
import sys

class FixedQueue:
    def __init__(self):
        self.que = [None] * 2000000
        self.front_ = 0 # 맨 앞 원소의 인덱스
        self.rear = 0   # 맨 뒤 원소의 인덱스 + 1 == 다음에 들어올 데이터의 인덱스
        self.no = 0 # 현재 데이터의 개수

    def push(self, value: Any) -> None: # enqueue
        self.que[self.rear] = value # rear의 자리에 더해줌
        self.rear += 1  # rear와 no를 1씩 증가
        self.no += 1

    def pop(self) -> Any:   # dequeue
        if self.empty():
            return -1
        else:
            x = self.que[self.front_]
            self.front_ += 1
            self.no -= 1
            return x        

    def size(self) -> int:
        return self.no

    def empty(self) -> None:
        if self.no <= 0:
            return 1
        else: return 0

    def front(self) -> int:
        if self.empty():
            return -1
        else:
            return self.que[self.front_]

    def back(self) -> int:
        if self.empty():
            return -1
        else:
            return self.que[self.rear - 1]


if __name__ == '__main__':
    input = sys.stdin.readline
    
    queue = FixedQueue()
    n = int(input())

    for i in range(n):
        order = input().strip()

        if order == 'pop':
            print(queue.pop())

        elif order == 'push':
            queue.push()

        elif order == 'size':
            print(queue.size())

        elif order == 'empty':
            print(queue.empty())

        elif order == 'front':
            print(queue.front())

        elif order == 'back':
            print(queue.back())

        else:
            _, value = order.split()
            queue.push(value)

