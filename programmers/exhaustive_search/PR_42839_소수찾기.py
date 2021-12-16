from itertools import permutations

def solution(numbers):        
    num_list = []
    for i in range(1, len(numbers)+1):
        for num in list(map(int, map(''.join, permutations(numbers, i)))):
            if find_prime(num):
                num_list.append(num)

    return len(set(num_list))

def find_prime(num: int):
    if num == 0 or num == 1:
        return 0
    if num == 2 or num == 3:
        return 1

    sqt = int(num ** 0.5)
    for i in range(2, sqt+1):
        if num % i == 0:
            return 0
    return 1