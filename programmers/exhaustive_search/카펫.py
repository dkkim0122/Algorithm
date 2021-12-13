def solution(brown, yellow):
    total = brown + yellow
    max = 0

    for i in range(2, int(total**0.5)+1):
        if total % i == 0 and i > max:
            max = i

    return [total // max, max]