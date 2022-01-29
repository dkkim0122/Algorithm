from collections import defaultdict, deque
from math import ceil

def solution(fees, records):
    data = defaultdict(list)
    base_time, base_cost, unit_time, unit_cost = fees
    result = []
    
    for record in records:
        time, num, inout = record.split()
        hour, min = time.split(":")
        time = [int(hour), int(min)]
        data[int(num)].append(time)
    
    data = sorted(data.items())

    for num, value in data:
        stack = []
        value = deque(value)
        total_time = 0
        while value:
            stack.append(value.popleft())
            if len(stack) == 2:
                total_time += dif(stack[0], stack[1])
                stack = []
        if stack:
            total_time += dif(stack[0], [23, 59])

        if total_time <= base_time:
            result.append(base_cost)
            continue
        else:
            cost = base_cost + ceil((total_time - base_time) / unit_time) * unit_cost
            result.append(cost)

    return result


def dif(time1, time2): # time = [h, m]
    h1, m1 = time1
    h2, m2 = time2
    hour = h2 - h1
    min = m2- m1
    if min < 0:
        hour -= 1
        min += 60
    return hour*60 + min

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))