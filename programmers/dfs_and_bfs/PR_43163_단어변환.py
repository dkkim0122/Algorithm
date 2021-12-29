from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [0] * len(words)

    return bfs(begin, words, target, visited)


def bfs(begin, words, target, visited):
    need_visit = deque([[begin, 0]])

    while need_visit:
        begin, count = need_visit.popleft()

        if begin == target:
            return count

        for i in range(len(words)):
            if visited[i] == 0:
                if comp_str(begin, words[i]) == 1:
                    visited[i] = 1
                    count += 1
                    need_visit.append([words[i], count])

    return 0

def comp_str(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    
    return count

