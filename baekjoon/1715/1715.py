# 최소값끼리 계속 더해나간다.

import heapq
import sys

input = sys.stdin.readline

n = int(input())
cards = []
count = 0

for i in range(n):
    card = int(input())
    heapq.heappush(cards, card) # min heap : 최솟값끼리 비교하면 되므로

while len(cards) > 1:
    temp1 = heapq.heappop(cards)
    temp2 = heapq.heappop(cards)
    sum = temp1 + temp2
    count += sum
    heapq.heappush(cards, sum)

print(count)