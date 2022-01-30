from collections import defaultdict

def solution(enroll, referral, seller, amount):
    # referral이 부모이다.
    parent_list = defaultdict(list)
    sell_list = defaultdict(list)
    money = defaultdict(int)

    for i, person in enumerate(enroll):
        parent_list[person] = referral[i]

    for i, person in enumerate(seller):
        sell_list[person] = amount[i] * 100
    
    def find(person, cost):
        if person == '-':
            money[person]+= cost
            return 

        parent = parent_list[person]
        for_parent = cost // 10
        if for_parent != 0:
            money[person] += cost - for_parent
            find(parent, for_parent)
        else:
            money[person] += cost
        return 

    for person, cost in sell_list.items():
        find(person, cost)
    
    answer = []
    for person in enroll:
        answer.append(money[person])

    return answer


    

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))