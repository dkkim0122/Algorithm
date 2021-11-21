import sys

input= sys.stdin.readline

def dfs(idx_op, total, plus, minus, multi, divide):
    if idx_op == n:
        result.append(total)
        return 
    
    if plus:
        dfs(idx_op+1, total + nums[idx_op], plus-1, minus, multi, divide)
    if minus:
        dfs(idx_op+1, total - nums[idx_op], plus, minus-1, multi, divide)
    if multi:
        dfs(idx_op+1, total * nums[idx_op], plus, minus, multi-1, divide)
    if divide:
        dfs(idx_op+1, total / nums[idx_op], plus, minus, multi, divide-1)

    return


n = int(input().strip())
nums = list(map(int, input().split()))
cal = list(map(int, input().split()))

print(nums)
print(cal)

result = []

dfs(1, nums[0], cal[0], cal[1], cal[2], cal[3])
print(max(result))
print(min(result))
