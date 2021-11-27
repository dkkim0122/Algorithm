import sys
input = sys.stdin.readline


if __name__=='__main__':
    test_num = int(input().strip())

    for _ in range(test_num):
        n = int(input().strip())

        grade = []
        for i in range(n):
            paper, interview = map(int, input().split())
            grade.append([paper, interview])

        grade.sort()

        count = 0
        paper, interview = grade[0]
        for i in range(n):
            if grade[i][0] <= paper or grade[i][1] <= interview:
                paper = grade[i][0]
                interview = grade[i][1]
                count += 1

        print(count)

