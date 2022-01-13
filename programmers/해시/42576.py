def solution(participant, completion):
    athelete = {}
    for p_name in participant:
        athelete[p_name] = athelete.get(p_name, 0) + 1
    for c_name in completion:
        athelete[c_name] -= 1
    for name in athelete:
        if athelete[name]:
            answer = name
    return answer