def solution(info, query):
    answer = []

    _info = []
    for i in info:
        _info.append(list(i.split()))
    
    _query = []
    for i in query:
        i = list(i.split(" and "))
        temp = i[-1].split()
        i[-1] = temp[0]
        i.append(temp[1])
        answer.append(make_check(_info, i))

    return answer

def make_check(_info, query_line):
    count = 0
    for i in _info:
        flag = True
        print(f'i : {i}')
        for j in range(5):
            if query_line[j] == '-':
                continue
            else:
                if j < 4 and query_line[j] != i[j]:
                    flag = False
                    break
                elif j == 4 and query_line[j] > i[j]:
                    flag = False
                    break

        if flag == True:
            count += 1
    return count

    

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))