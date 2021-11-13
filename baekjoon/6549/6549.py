while True:
    temp = list(map(int, input().split()))
    n = temp[0]
    if n == 0:
        break
    heights = temp[1:]

    heights.insert(0, 0)
    heights.append(0)

    # 스택에는 인덱스를 저장한다. 현재 인덱스의 높이보다 높은 애들만 남는다.
    # 현재 바로 전까지 모든 인덱스 중 그 전보다 높이가 상승한 애들의 인덱스만 남는다.
    check = [0] 
    area = 0

    for i in range(1, n+2):
        while check and heights[i] < heights[check[-1]]: 
        # 현재 높이가 전 높이보다 낮으면 낮아진 높이로 넓이를 계산한다.
        # 내 전 직사각형 중 나보다 높은 애들
            prev_idx = check.pop()
            # 스택에서 없애고 현재 인덱스에 저장한다.
            # 한 번 높이가 높아졌다 낮아지면 높았던 높이의 넓이는 최대치만 고려하면 되므로
            # 그 인덱스들은 이제 고려할 필요가 없기 때문이다. 
            area_in_prev_idx = (i-1-check[-1])*heights[prev_idx]
            # 직전 높이에서의 최대 넓이

            area = max(area, area_in_prev_idx)

        # 내 전보다 높이가 나보다 낮은 애들은 일단은 고려하지 않는다.
        # 뒤에 그 높이보다 낮은 높이가 나오면 그때 계산한다(하물며 맨 마지막으로 가서 0이랑 비교하든가)
        
        check.append(i)
        # 지금 인덱스를 스택에 저장한다.
        # 뒤에 나올 높이가 지금 높이보다 높다면 쭉 스택에 저장될 것이고
        # 낮다면 이 인덱스를 가지고 넓이를 계산할 것이다.

    print(area)