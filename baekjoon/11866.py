N, K = map(int, input().split())
lst = list(range(1, N+1))
result = []
point = K-1

for i in range(N):
    if len(lst) > point:
        result.append(lst.pop(point))
        point += K - 1
    elif len(lst) <= point:
        point = point % len(lst)
        result.append(lst.pop(point))
        point += K - 1

print("<", end='')
for i in result:
    if i == result[-1]:
        print(i, end='')
    else:
        print("%s, " %(i), end='')
print(">")