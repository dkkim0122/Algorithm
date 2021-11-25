import sys

def fib_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    fib_list = [0,1]

    for i in range(2, n+1):
        num = fib_list[i-1] + fib_list[i-2]
        fib_list.append(num)
    
    return fib_list[n]


if __name__ == '__main__':
    input = sys.stdin.readline

    n = int(input().strip())

    print(fib_dp(n))
