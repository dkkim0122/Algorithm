import sys
input = sys.stdin.readline



if __name__=='__main__':
    n, k = map(int, input().split())
    coins = [input().strip() for _ in range(k)]

    print(coins)
    
