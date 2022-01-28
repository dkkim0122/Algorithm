import sys
sys.setrecursionlimit(10**6)

def solution(numbers, target):
    result = []

    def dfs(count, total):
        if count == len(numbers):
            print(total)
            if total == target:
                result.append(total)
            return
        
        dfs(count+1, total + numbers[count])
        dfs(count+1, total - numbers[count])

        return

    dfs(0, 0)

    answer = len(result)
    return answer

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))