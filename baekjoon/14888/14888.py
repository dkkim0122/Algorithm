import sys
from itertools import permutations
import copy

input= sys.stdin.readline

def calculate(cal_perm):
    num = copy.deepcopy(nums) # 각 계산마다 nums를 수정하면 안 되므로 deepcopy
    for i in range(n-1):
        if cal_perm[i] == '+':
            num[i+1] = num[i]+num[i+1]
        elif cal_perm[i] =='-':
            num[i+1] = num[i]-num[i+1]
        elif cal_perm[i] =='*':
            num[i+1] = num[i]*num[i+1]
        elif cal_perm[i] == '//':
            if num[i]<0:
                num[i+1] = -((-num[i])//num[i+1]) # 문제 나눗셈 규정에 맞춰서
            else:
                num[i+1] = num[i]//num[i+1]
    
    return num[n-1]


n = int(input().strip())
nums = list(map(int, input().split()))
lst_lists = list(map(int, input().split()))
cal_lists = ['+','-','*','//']
cal = []
for i in range(len(lst_lists)):
    for j in range(lst_lists[i]):
        cal.append(cal_lists[i]) # 해당 입력받은 연산자들을 순서대로 나열

perm_list = list(permutations(cal)) # 가능한 연산자 순열을 나열
result = []

# print(calculate(['+','+','-','*','//']))

for perm in perm_list:
    result.append(calculate(perm))

print(max(result))
print(min(result))
                