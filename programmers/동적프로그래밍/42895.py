from collections import defaultdict

def solution(N, number):
    s = defaultdict(set)
    for i in range(1, 9):
        s[i].add(int(str(N)*i))
        for j in range(1, i):
            for n1 in s[j]:
                for n2 in s[i-j]:
                    operate = [n1 + n2, n1 - n2, n1 * n2]
                    if n2 != 0:
                        operate.append(n1 // n2)
                    for op_i in operate:
                        if op_i > 0:
                            s[i].add(op_i)
        if number in s[i]:
            return i
    return -1