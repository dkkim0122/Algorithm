def partitionLabels(s: str):
    from collections import defaultdict

    # last라는 딕셔너리에 각 문자들이 끝나는 가장 마지막 인덱스를 저장    
    last = {}
    for idx, char in enumerate(s):
        last[char] = idx
    
    part_end = 0
    part_begin = 0
    partitions = []

    # for문으로 문자들을 만나면서 각 문자들이 끝나는 지점을 조사한다.
    # 만약 끝나는 지점이 더 뒤에 있다면 
    # part는 적어도 그 지점까지는 확장되어야 한다.
    # 만약 그 part의 끝나는 지점까지 도달했으면 part는 끝나고,
    # 그때까지의 문자들을 하나의 part로써 저장하고 다시 그 뒤부터 탐색한다.
    for idx, char in enumerate(s):
        last_idx = last[char]
        part_end = max(part_end, last_idx)
        if idx == part_end:
            partitions.append(s[part_begin:part_end+1])
            part_begin = idx + 1

    return partitions