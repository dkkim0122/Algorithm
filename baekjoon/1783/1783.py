import sys
from collections import deque
input = sys.stdin.readline



if __name__=='__main__':
    Y, X = map(int, input().split())

    squares = 0

    if Y == 1:
        squares = 1
    elif Y == 2:
        squares = min(4, (X+1)//2)
    elif Y >= 3:
        if X <= 4:
            squares = X
        elif X==5 or X==6:
            squares = 4
        elif X >= 7:
            squares = X-7+5
    
    print(squares)
