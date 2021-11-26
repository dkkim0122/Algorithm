import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def find_lcs_recur(n, m):

    if n==0 or m==0: # lcs(0,...), lcs(...,0)의 값은 0이다.
        return 0

    # matrix의 row: len(str1), col: len(str2)이므로, 0번째 인덱스가 0이 아니다.
    # lcs(n, m)의 값을 matrix[n-1][m-1]에서 찾는다.
    if dp[n-1][m-1] != -1:
        return dp[n-1][m-1]

    str1_final_char = str1[n-1]
    str2_final_char = str2[m-1]

    if str1_final_char==str2_final_char:
        dp[n-1][m-1] = find_lcs_recur(n-1, m-1) + 1 # dp[n-1][m-1]의 값은 dp[n-2][m-2]에서.
    else:
        dp[n-1][m-1] = max(find_lcs_recur(n-1, m), find_lcs_recur(n, m-1))

    return dp[n-1][m-1]

if __name__=='__main__':
    str1 = input().strip()
    str2 = input().strip()

    dp = [[-1]*(len(str2)+1) for _ in range(len(str1)+1)] # default값을 -1로 둔다.

    print(find_lcs_recur(len(str1), len(str2)))