
def prod(a:list, b:list) -> list:
    n = len(a)
    product = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                product[i][j] += a[i][k] * b[k][j]  

    for i in range(n):
        for j in range(n):
            product[i][j] %= 1000      

    return product

def devide(mat: list, N: int) -> list:
    if N == 0:
        return
    if N == 1:
        return mat
    if N == 2:
        return prod(mat, mat)
    else:
        temp = devide(mat, N//2)
        if N % 2 == 0:
            return prod(temp, temp)
        else:
            return prod(prod(temp, temp), mat)

length, N = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(length)]

mat_devide = devide(mat, N)

for i in range(length):
    for j in range(length):
        mat_devide[i][j] %= 1000
        print(mat_devide[i][j], end=' ')
    print()