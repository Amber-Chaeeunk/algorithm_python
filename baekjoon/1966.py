cnt = 1

for i in range(int(input())):
    size, idx = map(int, input().split())
    lst = list(map(int, input().split()))
    print(c)
    if m < 2:
        print('1')
    elif 2 <= m <= 100:
        if max(c) == c[w]:
            print('1')
        else:
            while max(c) != c[w]:
                idx = c.index(max(c))
                c[idx] = 0
                cnt += 1
                # print(c)
            if max(c) == c[w]:

            print(cnt)
