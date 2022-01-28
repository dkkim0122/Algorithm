from collections import deque

def solution(number, k):
    number = deque(number)
    length = len(number) - k
    stack = deque([number.popleft()])
    count = 0
    
    while number:
        num = number.popleft()
        while count < k and stack and stack[-1] < num:
            stack.pop()
            count += 1
        stack.append(num)
    while len(stack) != length:
        stack.pop()

    return "".join(stack)

number = "77777"
k = 3
print(solution(number, k))