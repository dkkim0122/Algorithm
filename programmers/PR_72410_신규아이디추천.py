from collections import deque

def solution(new_id):
    answer = ''
    unavailable = set("~!@#$%^&*()=+[{]}:?,<>/")

    result = []
    result1 = []
    result2 = []
    result3 = []

    # step 1, 2
    new_id = deque(new_id)
    for i, ch in enumerate(new_id):
        if ord('A') <= ord(ch) <= ord('Z'):
            new_id[i] = new_id[i].lower()
        result.append(new_id[i])
    
    # step 3
    for i, ch in enumerate(result):
        if result[i] in unavailable:
            continue
        result2.append(result[i]) 
    result = result2
    print(result)

    for i, ch in enumerate(result):
        if i < len(result)-1 and result[i] == '.' and result[i+1] == '.':
            continue
        result3.append(result[i])
    result = result3
    print(result)


    # step 4
    while result and result[0] == '.':
        result = result[1:]
    while result and result[-1] == '.':
        result.pop()

    # step 5
    if len(result) == 0:
        result.append('a')
    
    # step 6
    if len(result) >= 16:
        result = result[:15]
    if result[-1] == '.':
        result = result[:-1]
    
    # step 7
    while len(result) <= 2:
        result.append(result[-1])

    return ''.join(result)

new_id = "....[]....a."
print(solution(new_id))