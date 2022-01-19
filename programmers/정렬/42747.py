def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations), 0, -1):
        if citations[i-1] >= i:
            return i
    return 0