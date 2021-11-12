def recur(x: int, y: int, N: int) -> None:
    # 0이면 끝인데, 밑에 판단 기준(모든 원소의 합)을 넣어뒀기 때문에 
    # N == 0 까지 안 간다.
    if N == 0:
        return

    # 판단
    # 굳이 원래의 리스트를 분할하지 않고, 그 좌표만 변경하면서 본다.
    # 원래처럼 새로 인덱스를 설정해줘야 하는 방법은
    # 새로운 리스트를 계속 설정해줘야 한다.

    # 모든 요소를 다 더해줄 필요가 없다. 
    # 색종이의 가장 첫 색깔과 다른 것이 있는지를 찾으면 된다.
    color = paper[x][y]

    for i in range(x, x + N):  # 첫 시작점에서 N 만큼
        for j in range(y, y + N):
            if color != paper[i][j]:  # 다른 게 하나라도 있으면
                recur(x, y, N//2)
                recur(x, y + N//2, N//2)    # 각 사분면의 시작점을 x, y로.
                recur(x + N//2, y, N//2)
                recur(x + N//2, y + N//2, N//2)
                return  # 여기까지만 해 주면 된다. 재귀 끝나고 밑으로 내려가는거 방지
    
    # 이 밑은 다른 게 하나도 없는 애들을 위해서
    # 만약 다 같은 색이다 : 종이의 처음 색깔과 동일하다.
    if color == 0:
        result.append(0)
    else:
        result.append(1)

result = []

lst = [2**i for i in range(1,8)]

while True:
    N = int(input())
    if N in lst:
        break

paper = [None] * N

for i in range(N):
    paper[i] = list(map(int, input().split()))

recur(0, 0, N)

print(result.count(0))
print(result.count(1))