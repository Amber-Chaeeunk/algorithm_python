import sys

n = int(input())
result = []

for i in range(n):
    name, check = map(str, sys.stdin.readline().split())
    if name not in result:
        result.append(name)
    else:
        result.remove(name)

for i in result:
    print(i)