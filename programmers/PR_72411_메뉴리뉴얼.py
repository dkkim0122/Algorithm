from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    menu = defaultdict(int)
    orders_set = []
    answer = []

    for order in orders:
        orders_set.append(set(order))

    length = len(orders_set)
    for i, order in enumerate(orders_set):
        for j in range(i+1, length):
            print(f'--------order = {order}, oders_set = {orders_set[j]}')
            common = list(order & orders_set[j])
            if common:
                for i in range(2, len(common)+1):
                    comb = list(combinations(common, i))
                    for com in comb:
                        menu[''.join(com)] += 1
                        print(f'common = {common}, com = {com}')
            
    print(menu)

    temp = [[] for _ in range(len(orders))]
    for key, value in menu.items():
        if len(key) in course:
            temp[value].append(key)

    print(temp)

    return answer

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

print(solution(orders, course))