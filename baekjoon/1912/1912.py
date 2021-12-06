# 양수들끼리 쭉 더하다가 음수를 만나면 그만하고 그 값을 max랑 비교 
# -> 안됨. 그 뒤에 엄청 큰 값이 나오면 더하는 게 이득 ex) 1, 2, -2, 10
# 계속 더하다가 음수를 만났을 때 그 합이 음수가 나오면, 그 전까지의 숫자를 저장하고 다시 시작

import sys
input = sys.stdin.readline


if __name__=='__main__':
    N = int(input().strip())
    lst = list(map(int, input().split()))
    dp = [0] * N

    dp[0] = lst[0]
    for i in range(1, N):
        if  + dp[i]

    print(summation)