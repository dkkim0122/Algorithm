import sys
input = sys.stdin.readline


def tsp(dists):
    N = len(dists)
    INF = float('inf')
    # cache[마지막 도시][그때까지의 경로] = 그 경로에 필요한 총 비용
    # cache와 bitmask를 사용함으로써 
    cache = [[None]*(1<<N) for _ in range(N)] # cache를 사용함으로써 해당 경로까지의 비용을 구할 수 있게 됐다.
    VISITED_ALL = (1<<N)-1 # N개의 자릿수가 모두 1

    # 해당 도착점과 총 경로 최소 비용을 찾아 캐시에 저장한다.
    def find_path(last, visited):
        # 3. 다 방문하였으면 끝과 시작을 잇는 경로의 비용을 리턴한다.
        if visited == VISITED_ALL:
            return dists[last][0] or INF # 시작점은 아무데나 상관없으므로, 그냥 0인덱스를 시작으로 하자
        
        # 만약 끝점이 last이고 경로가 visited인 경로까지의 비용을 이미 구했다면,
        # 그냥 그 값을 리턴해줘 중복을 방지한다(메모이제이션).
        if cache[last][visited] != None:  
            return cache[last][visited]

        # 1. 방문한 적이 없고, 이어져 있으면 계속해서 다른 도시들을 방문한다.
        # 2. 새로 찾은 도시를 추가하여 계속 방문한다
        # 4. 리턴받은 dists[last][0]부터 각 경로의 비용들 중 최소를 찾으면서 계속 더해 나간다.
        temp = INF
        for city in range(N):
            if visited & (1<<city) == 0 and dists[last][city] != 0:
                temp_cost = find_path(city, visited|(1<<city)) + dists[last][city]
                temp = min(temp, temp_cost)
        
        # 5. 해당 마지막 도시와 총 경로의 최소 비용을 캐시에 저장한다.
        cache[last][visited] = temp 
        return temp

    
    return find_path(0, 1<<0) # 시작점이 0이라 도착 지점도 0, visited도 01.


if __name__=='__main__':
    N = int(input().strip())    
    dists = []
    for _ in range(N):
        dists.append(list(map(int, input().split())))

    print(tsp(dists))
    

