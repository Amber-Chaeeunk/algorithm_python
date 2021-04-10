n = int(input())

for i in range(n):
    a = list(input())
    tmp = []
    cnt = 0
    for j in a:
        if j == "(":
            tmp.append(j)
        elif j == ")":
            if not tmp:
                print("NO")
                cnt = 1
                break
            else:
                tmp.pop()
    if not tmp and cnt == 0:
        print("YES")
    elif len(tmp) != 0 and cnt == 0:
        print("NO")



# import sys
#
# n = int(input())
#
# cnt = 0
#
# for i in range(n):
#     test = sys.stdin.readline().split()
#     for j in test:
#         print(j)
#         if j[0] != '(':
#             cnt = 1
#             break
#         for k in range(len(j)):
#             if j[k] == '(':
#                 cnt += 1
#             elif j[k] == ')':
#                 cnt -= 1
#             else:
#                 continue
#             if cnt == -1:
#                 cnt = 1
#                 break
#
#         if cnt == 0:
#             print('YES')
#         elif cnt != 0:
#             print('NO')
#
