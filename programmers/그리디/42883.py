def solution(number, k):
    answer = []
    for num in number:
        while answer and num > answer[-1]:
            if k > 0:
                answer.pop()
                k -= 1
            else:
                break
        answer.append(num)

    if k > 0:
        answer = answer[:-k]

    return ''.join(answer)