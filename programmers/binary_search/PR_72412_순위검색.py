from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)


    # info에 있는 조건들의 조합을 key로 하여 dictionary를 만든다.
    for i in info:
        i = i.split()
        info_key = i[:-1]
        info_val = i[-1]

        for j in range(5):
            for c in combinations(info_key, j):
                tmp = ''.join(c)
                info_dict[tmp].append(int(info_val)) # 한 key에 여러 value들이 존재할 수 있다.

    # info_dict 내의 val들 정렬 -> 여기서 미리 정렬하고 들어가는 것이 빠르다
    for k in info_dict:
        info_dict[k].sort()
            
    for i in query:
        i = i.split(" and ")
        temp = i[-1].split()
        i[-1] = temp[0]

        query_key = i
        query_val = int(temp[1])
        while '-' in query_key:
            query_key.remove('-')

        query_key = ''.join(query_key)

        # info_dict 중에서 key값이 query_key와 같은 key를 찾는다.
        # 해당 key의 value(리스트임)를 가져와서 query_val 이상인 값들의 개수를 찾는다.
        if query_key in info_dict:
            scores = info_dict[query_key]
            # scores.sort() # -> 여기서 해 버리면 query_key가 중복되는 경우도 계속 해야하기 때문에 느려진다.
            if scores:
                under_val = bisect_left(scores, query_val) # query_val과 같은 값이 있으면 그 앞의 인덱스를 찾아야 한다.
                answer.append(len(scores) - under_val) # query_val보다 큰 애들의 개수
        else: # query_key와 같은 값이 info_dict에 없으면 
            answer.append(0)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))