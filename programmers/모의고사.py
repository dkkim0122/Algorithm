def solution(answers):
    def check_ans(student, answers):
        correct = 0
        for i in range(len(answers)):
            if answers[i] == student[i % len(student)]:
                correct += 1
        
        return correct
    
    students = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    scores = [0] * 3
    result = []
    
    for i, student in enumerate(students):
        scores[i] = check_ans(student, answers)

    for i, score in enumerate(scores):
        if score == max(scores):
            result.append(i+1)

    return result