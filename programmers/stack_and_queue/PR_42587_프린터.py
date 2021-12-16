def solution(priorities, location):
    docs = [i for i in range(len(priorities))]
    result = []

    while docs:
        doc = docs.pop(0)
        if priorities[doc] < max(priorities):
            docs.append(doc)
        else:
            result.append(doc)
            priorities[doc] = 0

    return result.index(location) + 1
