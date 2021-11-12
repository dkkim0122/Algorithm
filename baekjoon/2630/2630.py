white = 0
blue = 0

def recur(a: list, N: list) -> list:
    global white, blue
    total = 0
    size  = N//2

    # 0이면 끝
    if N == 0:
        return
    # 판단
    # 모든 요소 다 더해봐서 
    for i in range(N):
        total += sum(a[i])

    # 0이면 다 흰색 N*N이면 다 파란색
    if total == 0:
        white += 1
        return
    elif total == N*N:
        blue += 1
        return

    a_quar1 = []
    a_quar2 = []
    a_quar3 = []
    a_quar4 = []

    # 4개로 나눈다.
    # 1 사분면 
    for i in range(size):
        a_quar1.append(a[i][:size])
    for i in range(size):
        a_quar2.append(a[i][size:N])
    for i in range(size, N):
        a_quar3.append(a[i][:size])
    for i in range(size, N):
        a_quar4.append(a[i][size:N])

    recur(a_quar1, N//2)
    recur(a_quar2, N//2)
    recur(a_quar3, N//2)
    recur(a_quar4, N//2)


N = int(input())

a = [None] * N

for i in range(N):
    a[i] = list(map(int, input().split()))

recur(a, N)

print(white, blue)