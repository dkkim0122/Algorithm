import sys
input = sys.stdin.readline


def find_min_cost():
    # 첫 번째 집은 costs 그대로
    # 두번째부터 R을 선택했으면, i-1번째 집에 B, G 중 최소가 되는 값을 가져와 costs[i][j]를 더한다.

    for i in range(num_house):
        if i == 0:
            dp[i] = costs[0]

        for j in range(3):
            dp[i][j] = min(dp[i-1][(j+1)%3]+costs[i][j], dp[i-1][(j-1)%3]+costs[i][j])

    return min(dp[num_house - 1])


if __name__=='__main__':
    num_house = int(input().strip())

    costs = [list(map(int, input().split())) for _ in range(num_house)]

    # dp[i][j] == i번째 집이 j색(R:0, G:1, B:2)을 고를 때, 그때까지의 최소 비용
    dp = [[0]*3 for _ in range(num_house)]

    print(find_min_cost())