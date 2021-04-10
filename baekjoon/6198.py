# import sys
#
# n = int(input())
#
# cnt = 0
# tmp = 0
# stack = []
#
# for i in range(n):
#     stack.append(int(sys.stdin.readline()))
#
# for i in range(n):
#     if len(stack) == n:
#         break
#     for j in range(n-i):
#
#         if stack[i] <= stack:
#         stack.pop()
#     else:
#         cnt += 1
#         tmp = stack[-1]
#         stack.pop()
#
# print(cnt)

import sys

n = int(sys.stdin.readline())
h = [int(sys.stdin.readline()) for _ in range(n)]
stack, cnt = [], 0
for i in range(n):
    while stack and stack[-1] <= h[i]:
        stack.pop()
    stack.append(h[i])
    cnt += len(stack)-1
print(cnt)