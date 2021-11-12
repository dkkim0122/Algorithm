import sys
input = sys.stdin.readline

def bin_search(house: list, key_count:int) -> int:
    start = 1   # just minimum distance
    end = house[-1] - house[0]
    ans = 0
    
    while start <= end:
        mid = (start + end)//2
        current_house = house[0]    # 앞집부터 설치
        count = 1   # 공유기 개수

        print(f'start = {start}')
        print(f'end = {end}')
        print(f'mid = {mid}')


        #지금 거리로 가능한 공유기 개수 count를 찾는다.
        for i in range(1, len(house)):  # 그 다음 공유기 찾기
            if house[i] >= current_house + mid: # 다음 공유기까지 거리가 키값보다 크다
                count += 1  
                current_house = house[i] # 거기서부터 다음 가능한 공유기를 찾는다.
            
        # 공유기 개수를 키 값으로 count와 비교한다.        
        if count >= key_count: # 공유기 개수가 키값보다 많다 
            ans = mid
            start = mid + 1 #-> 거리를 늘려도 되겠다.
        else:   # 공유기 개수가 키값보다 적다
            end = mid - 1   # -> 거리를 줄여야 되겠다.
    return ans


N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]

house.sort()

print(bin_search(house, C))


