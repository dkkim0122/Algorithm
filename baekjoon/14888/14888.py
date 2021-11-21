import sys
from itertools import permutations
input= sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))
lst_lists = list(map(int, input().split()))
cal_lists = ['+','-','*','//']
cal = []
for i in range(len(lst_lists)):
    for j in range(lst_lists[i]):
        cal.append(cal_lists[i])

print(nums)
print(lst_lists)
print(cal)

def calculate(cal_perm):
    for i in range(n-1):
        if cal_perm[i] == '+':
            nums[i+1] = nums[i]+nums[i+1]
        elif cal_perm[i] =='-':
            nums[i+1] = nums[i]-nums[i+1]
        elif cal_perm[i] =='*':
            nums[i+1] = nums[i]*nums[i+1]
        elif cal_perm[i] == '//':
            if nums[i]<0:
                nums[i+1] = -((-nums[i])//nums[i+1])
            else:
                nums[i+1] = nums[i]//nums[i+1]
    
    return nums[n-1]


perm_list = list(permutations(cal))
result = []


for perm in perm_list:
    result.append(calculate(perm))

print(max(result))
print(min(result))
                