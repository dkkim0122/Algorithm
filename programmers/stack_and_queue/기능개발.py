from collections import deque

progresses = [93, 30, 55]
speeds = [1, 30 ,5]

queue = deque(progresses)
answer = []

while queue:
    count = 0
    for i, func in enumerate(queue):
        func += speeds[i]
    
    while queue[0] >= 100:
        queue.popleft()
        count += 1
    
    answer.append(count)

print(answer)