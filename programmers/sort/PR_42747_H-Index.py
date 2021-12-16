def solution(citations):
    n = len(citations)
    max_h = 0
    for h in range(max(citations)):
        count_h = 0
        for paper in citations:
            if paper >= h: 
                count_h += 1
        if count_h >= h:
            max_h = max(max_h, h)
        
    return max_h