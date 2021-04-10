while True:
    s = input()
    if s == '.':
        break
    tmp = []
    result = True
    for j in s:
        if j == "(" or j == "[":
            tmp.append(j)
        elif j == ")":
            if not tmp or tmp[-1] == "[":
                result = False
                break
            elif tmp[-1] == "(":
                tmp.pop()
        elif j == "]":
            if not tmp or tmp[-1] == "(":
                result = False
                break
            elif tmp[-1] == "[":
                tmp.pop()
    if not tmp and result == True:
        print("yes")
    else:
        print("no")