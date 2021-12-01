import sys
input = sys.stdin.readline

def check_lis(lst):
    dp = [1] * len(lst)

    for i, num in enumerate(lst):
        for j in range(0, i):
            if num > lst[j]:
                dp[i] = max(dp[i], dp[j]+1)
    
    return max(dp)


if __name__ == '__main__':
    N = int(input().strip())
    lines = [list(map(int, input().split())) for _ in range(N)]
    lines.sort()

    b_nums = []
    for a, b in lines:
        b_nums.append(b)

    print(N-check_lis(b_nums))