# map()을 이용해서 코드 간결하게 줄이기.

import sys
input = sys.stdin.readline

num_test = int(input())

case = []

for i in range(num_test):
    a, b = map(int, input().split())
    case.append(a + b)

for i in range(num_test):
    print(case[i])
