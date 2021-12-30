from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    return bfs(begin, words, target)


def bfs(begin, words, target):
    need_visit = deque([[begin, 0]])

    while need_visit:
        begin, count = need_visit.popleft()

        if begin == target:
            return count

        count += 1
        
        for i in range(len(words)):
            if comp_str(begin, words[i]) == 1:
                need_visit.append([words[i], count])

    return 0

def comp_str(str1, str2):
    count = 0
    for a, b in zip(str1, str2):
        if a != b:
            count += 1
    
    return count

