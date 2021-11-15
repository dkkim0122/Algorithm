import sys
input = sys.stdin.readline

def cal_circles(circles: list) -> int:
    coord = []
    stack = []

    # 좌표를 원 왼쪽 점 0, 오른쪽 점 1로 나눈 후 정렬
    # [2,12], [-20,2], [2,20], [-20,20]의 경우 
    # [0,2],[1,12],[0,-20],[1,2],[0,2],[1,20],[0,-20],[1,20]
    # 정렬 후 [1,12],[1,2],[1,20],[1,20],[0,2],[0,-20],[0,2],[0,-20]
    # 정렬 후 [0,-20],[0,-20],[1,2],[0,2],[0,2],[1,12],[1,20],[1,20]
    for circle in circles:
        left = circle[0]
        right = circle[1]
        coord.append([0, left])
        coord.append([1, right])

    coord = sorted(coord, reverse=True) # 먼저 오른쪽 -> 왼쪽 순으로 정렬한 다음
    coord = sorted(coord, key = lambda x:x[1]) # 같은 좌표 상 오른쪽이 먼저 오게(원을 닫는 것을 먼저)

   
    # stack 원소에 원을 넣을 때는 [2, 지름]으로 push한다. 
    
    # 스택에서 바로 최근 원소(가장 가까운 왼쪽 좌표)를 pop해 이 원의 지름을 구한다.
    # 

    count = 1

    for lr, x in coord:
        if lr == 0:  # 원이 열릴 때
            stack.append([lr, x])
        else:   # 원이 닫힐 때
            sum_diameter = 0  # 일단 원의 지름의 합을 넣는 변수 sum_diameter를 만든다
            while stack and stack[-1][0] == 2: # 만약 stack 가장 최근 원소가 원이면 
                _, complete_circle = stack.pop() # 다시 pop해준 다음 
                sum_diameter += complete_circle # 해당 지름을 diameter에 더해준다.

            diameter = x - stack.pop()[1]   # 지름을 구한다

            if diameter == sum_diameter:    # 만약 지금까지 더한 지름의 합이 해당 원 지름과 같다면 끊김없이 붙어있는 것.
                count += 2
            else:
                count += 1
            stack.append([2, diameter])


    return count


if __name__ == '__main__':
    n = int(input())
    circles = [None] * n

    for i in range(n):
        x, r = map(int, input().split())
        left = x - r
        right = x + r
        circles[i] = [left, right]

    print(cal_circles(circles))
