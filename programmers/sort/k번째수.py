def solution(array, commands):
    answer = []
    
    for start, end, target in commands:
        arr = array[start-1:end]
        arr.sort()
        ans = arr[target-1]
        answer.append(ans)  
    
    return answer