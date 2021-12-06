
def bin_search(a: list) -> int:
    n = len(a)
    start = 0
    end = n -1
    standard = max(abs((a[0]) + a[1]), abs(a[-1] + a[-2])) # 가장 max인 값
    ans =[0, 0]

    while start < end:
        sum = a[start] + a[end]
        if abs(sum) <= abs(standard):
            ans = [a[start], a[end]]
            standard = sum
        if standard == 0:
            break
        if sum < 0: # 음수가 더 큼
            start += 1# 음수를 줄여줘야지
        else:
            end -= 1
    return ans

n = int(input())

liq = list(map(int, input().split()))

liq.sort()
one, two = bin_search(liq)
print(one, two)