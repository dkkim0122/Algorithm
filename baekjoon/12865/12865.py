import sys
input = sys.stdin.readline

# dp[i][j]의 의미는, 1) 최대 가방 무게가 j일 때
# 2) i번째 물건이 가방에 있을 수도 있고, 없을 수도 있을 때 그 둘 중 더 큰 가치의 값을 나타낸다.
# i번째 물건이 가방에 없다면 
# a) [(i-1개의 물건이 가방에 있고 최대 무게가 j에서 i번째 물건의 무게를 뺀 값의 가치) + (i번째 물건의 가치)]와
# b) [i-1개의 물건이 가방에 있고 최대 무게가 그대로 j]인 두 값 중 큰 것의 값과 같다.
# 즉 dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i]).
def knap_sack_recur(weight, value):
    dp = [[0] * (limit_weight+1) for _ in range(num+1)]
    for i in range(1, num+1):
        for j in range(1, limit_weight+1):
            if j >= weight[i]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[num][limit_weight]

    
if __name__=='__main__':
    num, limit_weight = map(int, input().split())
    weight = [0]*(num+1)
    value = [0]*(num+1)

    for i in range(1, num+1):
        w, v = map(int, input().split())            
        weight[i] = w
        value[i] = v

    print(knap_sack_recur(weight, value))