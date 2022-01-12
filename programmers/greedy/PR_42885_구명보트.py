from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    answer = 0

    stack = []
    count = 0
    while people:
        if count + people[0] <= limit:
            person = people.popleft()
            count += person
            stack.append(person)
        else:
            answer += 1
            count = 0
            stack = []

    answer += 1  # 마지막 구명보트

    return answer

people = [70, 80, 50]
limit = 100

print(solution(people, limit))