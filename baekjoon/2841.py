★핵심: 2차원 배열만들기 > 리스트 내의 리스트 > 각 1차원에서 구분되는 리스트는 기타줄만큼 미리 다 만들어주기


import sys

N, P = map(int, input().split())

move = 0
stack = [[] for i in range(7)]

for i in range(N):
    m, p = map(int, sys.stdin.readline().split())

    if len(stack[m]) == 0:
        move += 1
        stack[m].append(p)
    else:
        if p == stack[m][-1]:
            continue
        elif p > stack[m][-1]:
            move += 1
            stack[m].append(p)
        else:
            while stack[m] and p < stack[m][-1]:
                move += 1
                stack[m].pop()
            if stack[m] and p == stack[m][-1]:
                continue
            else:
                move += 1
                stack[m].append(p)
print(move)