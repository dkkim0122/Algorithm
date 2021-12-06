# 1 : 1
# 2 : 11 00
# 3 : 1+'00':100 / 2+'1':111, 001
# 4 : 2+'00':1100, 0000 / 3+'1':1001,1111,0011
# 즉, 길이가 n인 모든 2진 수열
# == n-2인 수열 뒤에 '00'을 붙인 값 + n-1인 수열 뒤에 '1'을 붙인 값

import sys

def dp_tiles(n):
    if n == 1:
        return 1
    elif n== 2:
        return 2
    
    tile_list = [0,1,2]

    for i in range(3, n+1):
        num = (tile_list[1] + tile_list[2])
        tile_list[1] = tile_list[2]
        tile_list[2] = num

    return tile_list[len(tile_list)-1]


if __name__=='__main__':
    input = sys.stdin.readline

    n = int(input())

    print(dp_tiles(n))
