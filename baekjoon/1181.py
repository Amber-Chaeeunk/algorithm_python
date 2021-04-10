n = int(input())
words = []

for i in range(n):
    words.append(input().lower())
tmp = 0
for i in words:
    for j in range(len(word)):
        if len(words[i]) > len(words[j]):
            tmp = words[i]
            words[i] = words[j]
            words[j] = tmp
        elif len(words[i]) == lend(words[j]):
            for k in range(len(word[i])):
                if ascii(words[i][k]) > ascii(words[j][k]):
                    tmp = words[i]
                    words[i] = words[j]
                    words[j] = tmp
                else:
                    continue
        else:
            continue





print(words)