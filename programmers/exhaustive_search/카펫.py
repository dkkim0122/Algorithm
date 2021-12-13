def solution(brown, yellow):
    lst = []
    result = []
    row = 0
    sqr = int(yellow**0.5)

    for i in range(1, sqr+1):
        if yellow % i == 0:
            y_row = max(i, yellow//i)
            y_col = min(i, yellow//i)
            if brown == ((y_row + y_col)*2 + 4):
                return (y_row + 2, y_col + 2)