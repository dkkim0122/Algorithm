# 가장 무게를 적게 담을 수 있는 가방부터 최댓값을 집어넣는다

import sys
input = sys.stdin.readline


if __name__=='__main__':
    jewel_num, bag_num = map(int, input().strip())
    jewels = [list(map(int, input().split())) for _ in range(jewel_num)]
    max_weight = [list(map(int, input().split())) for _ in range(bag_num)]

    jewels.sort()

    jewel_in_bag = []

    for i in 

