def solution(people, limit):
    people.sort()
    left = 0
    right = len(people) -1

    answer = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    return answer
