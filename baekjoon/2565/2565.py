import sys
input = sys.stdin.readline

if __name__=='__main__':
    INF = sys.maxsize
    city_num = int(input().strip())

    roads = list(map(int, input().split()))
    cities = list(map(int, input().split()))

    cost = 0
    min_cost = INF
    for i in range(len(cities)-1):
        if cities[i] < min_cost:
            min_cost = cities[i]
        cost += roads[i] * min_cost

    print(cost)
        
