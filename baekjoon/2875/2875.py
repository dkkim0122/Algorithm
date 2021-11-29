import sys
input = sys.stdin.readline

def make_team(girl, boy):
    if girl < 0 or boy < 0:
        return 0

    if girl < 2:
        return 0
    elif boy >= girl//2:
        return girl//2
    elif boy < girl//2:
        return boy

if __name__=='__main__':
    girls, boys, interns = map(int, input().split())

    # 매번 최대의 값을 찾아 나가므로 그리디...?
    max_teams = 0
    for i in range(interns+1):
        team_num = make_team(girls-i, boys-(interns - i))
        max_teams = max(max_teams, team_num)

    print(max_teams)
