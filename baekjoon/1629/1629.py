# 규칙이 있는데...
# 모듈러 연산(%)의 분배법칙이 있음

def recur(n: int, m: int):
    if m == 1:
        return n % a

    temp = recur(n, m//2)
    
    if m % 2 == 0:
        return (temp * temp) % a
    else:
        return (temp * temp * n) % a

n, m, a = map(int, input().split())

print(recur(n, m))