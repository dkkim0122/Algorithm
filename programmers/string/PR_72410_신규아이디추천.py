from collections import deque

def solution(new_id):
    unavailable = set("~!@#$%^&*()=+[{]}:?,<>/")

    result = []

    # step 1
    new_id = new_id.lower()
    
    # step 2
    for i in unavailable:
        new_id = new_id.replace(i, '')

    # step 3
    while ".." in new_id:
        new_id = new_id.replace('..', '.')

    result = list(new_id) 
    # step 4
    if result and result[0] == '.':
        result = result[1:]
    if result and result[-1] == '.':
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

new_id = "..!@$..[]....a."
print(solution(new_id))