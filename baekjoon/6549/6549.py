import sys
sys.setrecursionlimit(1000000)

def recur(h: int, a: list) -> int:
    n = len(a)
    max_area = 0
    area = 0

    if h == 0:
        return 0
    
    # 각 원소들과의 대소 비교를 통해서 영역을 구한다.
    for i in range(n):
        if a[i] >= h:   # 해당 원소가 기준보다 크다면
            area += h   # 넓이를 누적한다.
            if area >= max_area:
                max_area = area
        else:  # 해당 원소가 기준보다 작다면
            area = 0

    before_area = recur(h-1, a)

    if max_area > before_area:
        return max_area
    else:
        return before_area
                

lst_list = []

while True:
    lst = list(map(int,input().split()))
    if lst[0] == 0:
        break
    lst_list.append(lst)

for lst in lst_list:
    print(recur(max(lst), lst[1:]))

