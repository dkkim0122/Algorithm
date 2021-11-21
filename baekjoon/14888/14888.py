import sys

input= sys.stdin.readline

def dfs(idx_op, total, plus, minus, multi, divide): # 1,0,1,0이 들어왔으면은
    if idx_op == n:
        result.append(total)
        return # 리턴값이 없으므로 다 끝나면 재귀 밖으로 리턴값 주지 않고 여기서 끝난다.
    
    # elif로 연결된 게 아니라 if로 연결되어있어서 이런 재귀를 짤 수 있다.
    if plus:
        dfs(idx_op+1, total + nums[idx_op], plus-1, minus, multi, divide) # 이 쪽에서 1,0,1,0 -> 0,0,1,0으로 재귀 한 번
    if minus:
        dfs(idx_op+1, total - nums[idx_op], plus, minus-1, multi, divide) # 이 쪽에서는 안 하고
    if multi:
        dfs(idx_op+1, total * nums[idx_op], plus, minus, multi-1, divide) # 이 쪽에서 1,0,1,0 -> 1,0,0,0으로 재귀 돌고
    if divide:                                                                
        if total >= 0:
            dfs(idx_op+1, total // nums[idx_op], plus, minus, multi, divide-1) # 이 쪽에서도 안 함 
        else:
            dfs(idx_op+1, -(-total // nums[idx_op]), plus, minus, multi, divide-1) 

    return


n = int(input().strip())
nums = list(map(int, input().split()))
cal = list(map(int, input().split()))

result = []

dfs(1, nums[0], cal[0], cal[1], cal[2], cal[3])
print(max(result))
print(min(result))
