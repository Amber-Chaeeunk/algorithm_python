import sys

n = int(input())

cnt = 0
tmp = 0
stack = []

for i in range(n):
    stack.append(int(sys.stdin.readline()))

for i in range(n):
    if len(stack) == n:
        cnt += 1
        tmp = stack[-1]
        stack.pop()
    elif stack[-1] <= tmp:
        stack.pop()
    else:
        cnt += 1
        tmp = stack[-1]
        stack.pop()

print(cnt)