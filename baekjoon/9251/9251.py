import sys
input = sys.stdin.readline

def find_lcs(str1, str2):
    row = len(str1)
    col = len(str2)

    dp = [[0]*(col+1) for _ in range(row+1)]

    for i in range(0, row+1):
        for j in range(0, col+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # for i in dp:
    #     print(i)
    return dp[row][col]

if __name__=='__main__':
    str1 = input().strip()
    str2 = input().strip()

    print(find_lcs(str1, str2))