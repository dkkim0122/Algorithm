import sys
input = sys.stdin.readline

def find_m(k, leng, n):
    if k == 0:  # 초기값
        if n == 0:
            return 'm'
        else:
            return 'o'

    len_before = (leng-k-3)//2

    if 0 <= n < len_before:
        return find_m(k-1, len_before, n)
    elif n == len_before:
        return 'm'
    elif len_before < n < len_before + (3+k):
        return 'o'
    elif n >= len_before + (3+k):
        return find_m(k-1, len_before, n-((3+k)+len_before))


if __name__ == '__main__':
    n = int(input())

    # n이 속해 있는 S(k)의 k값을 구하라.
    k = 0
    leng = 3
    while n > leng:
        k += 1
        leng = leng*2 + k + 3

    print(find_m(k, leng, n-1))