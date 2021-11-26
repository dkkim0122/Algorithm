# 식의 최솟값을 구하기 위해서는 가장 작은 값에서 가장 큰 값을 빼야 한다.
# 마이너스를 만날 때 가장 큰 값을 빼 주면 된다.
# 마이너스를 만나면 다음 마이너스를 만날 때까지 계속 더해준다.


import sys

if __name__=='__main__':
    exp = list(input().split('-'))

    total = 0
    
    # 맨 첫 자리일 때는 항상 양수이다.
    nums = list(map(int, exp[0].split('+')))
    total += sum(nums)

    for i in range(1, len(exp)):
        nums = list(map(int, exp[i].split('+')))
        total -= sum(nums)

    print(total)