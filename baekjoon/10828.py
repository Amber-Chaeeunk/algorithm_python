import sys

n = int(input())

stack = []

for i in range(n):
    command = sys.stdin.readline().strip()

    if command.split()[0] == 'push':
        stack.append(command.split()[1])

    elif command == 'top':
        if not stack:
            print('-1')
        else:
            print(stack[-1])

    elif command == 'size':
        print(len(stack))

    elif command == 'pop':
        if not stack:
            print('-1')
        else:
            print(stack[-1])
            stack.pop()

    elif command == 'empty':
        if not stack:
            print('1')
        else:
            print('0')


