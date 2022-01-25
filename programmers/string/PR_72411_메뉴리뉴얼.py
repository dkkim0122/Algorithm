from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    for i in course:
        temp = []
        for order in orders:
            comb = combinations(sorted(order), i)
            temp += comb
        counter = Counter(temp)
        if counter and max(counter.values()) > 1:
            for com, value in counter.items():
                if value == max(counter.values()):
                    answer.append(''.join(com))
            
    return sorted(answer)

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

print(solution(orders, course))