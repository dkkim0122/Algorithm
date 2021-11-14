from typing import Any
import sys
input = sys.stdin.readline

class FixedStack:
    def __init__(self) -> None:
        self.stk = [None] * 10000 
        self.ptr = 0

    def push(self, value: Any) -> None:
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.empty():
            return -1
        self.ptr -= 1
        return self.stk[self.ptr]

    def size(self) -> int:
        return self.ptr

    def empty(self) -> int:
        if self.ptr <= 0:
            return 1
        else:
            return 0
    
    def top(self) -> Any:
        if self.empty():
            return -1
        else:
            return self.stk[self.ptr - 1]            

n = int(input())

stack = FixedStack()

for i in range(n):
    lst = input().strip()
    
    if lst == 'pop':
        print(stack.pop())
    elif lst == 'size':
        print(stack.size())
    elif lst == 'empty':
        print(stack.empty())
    elif lst == 'top':
        print(stack.top())
    else:
        order = lst.split()
        value = int(order[1])
        stack.push(value)