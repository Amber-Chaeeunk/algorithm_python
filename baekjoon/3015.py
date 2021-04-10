import sys

n = int(input())

cnt = 0
stack = []
tmp = []

for i in range(n):
    stack.append(int(sys.stdin.readline()))

for i in range(n-1):
    cnt += 1
    if i < n - 2:
        k = i + 1
        tmp.append(stack[k])
        k += 1
        for j in range(n-i-2):
            if min(stack[i], stack[k]) >= max(tmp):
                cnt += 1
                tmp.append(stack[k])
                k += 1
            else:
                if stack[i] < max(tmp):
                    break
                else:
                    tmp.append(stack[k])
                    k += 1
    del tmp[:]
print(cnt)
