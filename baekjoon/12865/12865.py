import sys
input = sys.stdin.readline

def find_max_value():
    for i in range(limit_weight+1):
        for weight in items:
            if (i-weight) in items and weight != (i-weight):
                dp[i] = max(dp[i], dp[weight]+dp[i-weight])
    print(dp)
    return dp[limit_weight]


if __name__=='__main__':
    num, limit_weight = map(int, input().split())
    dp = [0] * (limit_weight+1)  # 각 idx가 무게, 값이 그 무게에서의 최대 가치
    items = []

    for i in range(num):
        weight, value = map(int, input().split())            
        dp[weight] = value
        items.append(weight)

    print(find_max_value())