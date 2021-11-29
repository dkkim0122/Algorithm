import sys
input = sys.stdin.readline


if __name__=='__main__':
    multi_num, item_num = map(int, input().split())
    items = list(map(int, input().split()))
    multi = []
    count = 0
    INF = sys.maxsize


    for i in range(len(items)):
        if items[i] in multi:  # 만약 아이템이 콘센트에 꽂혀 있다면
            continue
        
        if len(multi) < multi_num: # 만약 멀티탭에 아직 남은 구멍이 있다면
            multi.append(items[i])
            continue

        # 콘센트에 꽂힌 용품이 다음번에도 쓰인다면 그 인덱스를 저장. 
        # index()는 같은 값이 여러 개 있을 때 가장 먼저 등장하는 인덱스를 저장한다.
        # 콘센트에 꽂힌 용품이 더 이상 안 쓰인다면 그 인덱스를 최대로 만들어 저장한다.
        # 인덱스들을 모아 놓았을 때 그 중 최대의 인덱스
        # (한 번도 쓰일 계획이 없거나, 있으면 그 중 가장 마지막에 처음으로 등장하는 용품)
        # 을 지닌 값을 교체한다.
        indices = []
        for multi_item in multi:
            try: 
                idx = items[i:].index(multi_item)
            except: 
                idx = INF
            indices.append(idx)  # 멀티탭에 꽂혀있는 순서대로 인덱스를 입력받는다.
        plug_out = indices.index(max(indices)) 
        multi[plug_out] = items[i]
        count += 1
    
    print(count)