from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    answer = 0

    while len(people) >= 2:
        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
        else:
            people.pop()
        answer += 1

    if people:
        return answer + 1
    else:
        return answer

people = [70, 30, 30, 70]
limit = 100

print(solution(people, limit))