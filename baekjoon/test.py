import sys
input = sys.stdin.readline


if __name__=='__main__':
    test_num = int(input().strip())
    for _ in range(test_num):
        temp = list(map(int, input().split()))
        num, scores = temp[0], temp[1:]

        avg = sum(scores) / num
        cnt = 0
        for score in scores: 
            if score > avg:
                cnt += 1
        
        ratio = cnt/num * 100
        print(f'{ratio:0.3f}%')