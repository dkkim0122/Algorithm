# 동적 프로그래밍
# 특정 범위까지의 값을 구하기 위해서 그것과 다른 범위까지의 값을 이용하여 
# 효율적으로 값을 구하는 알고리즘 설계 기법

from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

dp = []    # dp는 자기 자신 포함 만들 수 있는 부분 수열 크기
# 인덱스 : LIS의 길이
# 값 : 해당 길이의 LIS 중의 최댓값(오른쪽 값)

# bisect_left(arr, x): arr가 정렬되어있다는 가정하에 x값이 들어갈 위치 반환
for i in range(n):
    idx = bisect_left(dp, lst[i]) # 해당 값을 최댓값으로 가질 수 있는 LIS의 길이(dp의 인덱스)
    if len(dp) <= idx:  # 해당 값이 모든 dp에 대해 최댓값이다 -> LIS에 원소 하나 더해서 증가시킬 수 있다.
        dp.append(lst[i]) # 더 큰 dp 원소를 추가할 수 있다.
    else:   # 그렇지 않으면
        dp[idx] = lst[i]  # 더 작은 값으로 교체한다.

print(len(dp))