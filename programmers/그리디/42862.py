def solution(n, lost, reserve):
    new_reserve = set(reserve) - set(lost)
    lost = list(set(lost) - set(reserve))
    for i in new_reserve:
        for j in lost:
            if i in [j+1, j-1]:
                lost.remove(j)
    answer = n - len(lost)
    
    return answer