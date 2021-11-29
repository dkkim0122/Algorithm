import sys
input = sys.stdin.readline

if __name__=='__main__':
    girls, boys, interns = map(int, input().split())

    for i in range(interns):
        if girls//2 >= boys:
            girls -= 1
        else:
            boys -= 1

    print(min(girls//2, boys))