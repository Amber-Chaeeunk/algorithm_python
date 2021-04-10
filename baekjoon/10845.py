import sys

n = int(input())

stack = []

for i in range(n):
    command = sys.stdin.readline().rstrip()

    if command.split()[0] == 'push':
        stack.append(int(command.split()[1]))

    elif command == 'front':
        if not stack:
            print('-1')
        else:
            print(stack[0])

    elif command == 'back':
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
            print(stack[0])
            stack.pop(0)

    elif command == 'empty':
        if not stack:
            print('1')
        else:
            print('0')