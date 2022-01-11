import itertools

def solution(numbers):
    answer = 0
    lst = []
    for i in range(1, len(numbers)+1):
        lst.append(list(set(map(''.join, itertools.permutations(list(numbers), i)))))
    lst = set(map(int, sum(lst, [])))
    for i in lst:
        prime_num = True
        if i in [0, 1]:
            continue
        for j in range(2, i):
            if i%j == 0:
                prime_num = False
                break
        if prime_num:
            answer += 1
            
    return answer
 
