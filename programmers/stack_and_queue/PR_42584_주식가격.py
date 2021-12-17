def solution(prices):
    answer = []
    for i, price in enumerate(prices):
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if price > prices[j]:
                break

        answer.append(count)

    return answer
