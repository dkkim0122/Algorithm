import bisect

def solution(operations):
    queue = []

    for operartion in operations:
        oper, num = operartion.split()
        num = int(num)
        if oper == 'I':
            if queue:
                bisect.insort(queue, num)
            else:
                queue.append(num)
                
        else:
            if len(queue) > 0:
                if num == 1:
                    queue.pop()
                else:
                    queue.pop(0)
            else:
                continue

    if len(queue) >= 2:
        return [queue.pop(), queue.pop(0)]
    elif 1 <= len(queue) < 2:
        return [queue[0], queue[0]]
    else:
        return [0,0]

def bisect_search(lst, value):
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end)//2
        if lst[mid] <= value:
            if lst[mid] == value:
                return mid
            else:
                start = mid + 1
        else:
            end = mid - 1

    return start

lst = [-3, 1, 4, 6, 8, 9]
for i in range(-5, 12):
    print(bisect_search(lst, i))
