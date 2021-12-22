from collections import deque

def solution(operations):
    queue = deque([])

    for operartion in operations:
        oper, num = operartion.split()
        num = int(num)
        if oper == 'I':
            queue.append(num)
            queue = deque(sorted(queue))
        else:
            if len(queue) > 0:
                if num == 1:
                    queue.pop()
                else:
                    queue.popleft()
            else:
                continue

    if len(queue) >= 2:
        return [queue.pop(), queue.popleft()]
    elif 1 <= len(queue) < 2:
        return [queue[0], queue[0]]
    else:
        return [0,0]