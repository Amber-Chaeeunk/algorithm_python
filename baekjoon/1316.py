n = int(input())
cnt = 0

for i in range(n):
    group = input().lower()
    result = 0
    # group = list(input())
    for j in range(len(group)):
        if group.find(group[j], j+1) - j > 1:
            result = -1
            break
        else:
            result = 1
    if result == 1:
        cnt += 1
    else:
        continue

print(cnt)

