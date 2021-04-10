# n = int(input())
# num = list(input())
#
# ans=0
# for i in num:
#     ans = ans+int(i)
#     #ans += int(i)
#
# print(ans)

#list안에 문자열을 넣으면? 문자 하나하나가 리스트의 요소가 됨

import numpy as np
n = 50
d=1
x = np.random.uniform(-1, 1, (n,d))

print(x)
weight=np.array([[5],])
bias=np.array([10])

y = x @ weight + bias
print(y)

# a = np.array([[5,2],])
# a = np.array([5,2])
# print(a)