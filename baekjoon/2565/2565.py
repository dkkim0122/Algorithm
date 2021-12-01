import sys
input = sys.stdin.readline

def check(lines):
    for i in range(len(lines)):
        for j in range(i,len(lines)):
            if lines[i][1] > lines[j][1]:
                dp[i] += 1
                dp[j] += 1
    return dp

if __name__ == '__main__':
    N = int(input().strip())
    lines = [list(map(int, input().split())) for _ in range(N)]


    lines.sort()

    cnt = 0

    while True:
        dp = [0] * N

        result = check(lines)
        
        if result.count(0) == N:
            break

        max = 0
        max_idx = 0
        for idx, num in enumerate(result):
            if num > max:
                max = num
                max_idx = idx

        del lines[max_idx]
        cnt += 1

    print(cnt)