import sys
input = sys.stdin.readline

def find_minimum_num(coin_list, target) -> int:
    count = 0
    left_charge = target
    
    for coin in coin_list:
        count += left_charge // coin
        left_charge %= coin
    
    return count

if __name__=='__main__':
    n, k = map(int, input().split())

    coins = [int(input().strip()) for _ in range(n)]
    coins.sort(reverse=True)

    print(find_minimum_num(coins, k))