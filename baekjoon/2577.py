n = list(input())
m = 1

for i in n:
    m = m * int(i)

obj = list(str(m))
ans = [0,1,2,3,4,5,6,7,8,9]

for j in obj:
    idx = j
    i = i + 1

for j in obj:
    if int(j) == 0:
        a = a + 1
    elif int(j) == 1:
        b = b + 1
    elif int(j) == 2:
        c = c + 1
    elif int(j) == 3:
        d = d + 1
    elif int(j) == 4:
        e = e + 1
    elif int(j) == 5:
        f = f + 1
    elif int(j) == 6:
        g = g + 1
    elif int(j) == 7:
        h = h + 1
    elif int(j) == 8:
        i = i + 1
    else:
        k = k + 1