s = list(input())
tmp = 0

for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if s[i] < s[j]:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
        else:
            continue
for k in range(len(s)):
    print(s[k], end='')