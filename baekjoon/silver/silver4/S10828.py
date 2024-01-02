from collections import deque

T = int(input())
stack = deque()

for _ in range(T):
    operation = input().split()

    if operation[0] == 'push':
        stack.append(operation[1])
    elif operation[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif operation[0] == 'size':
        print(len(stack))
    elif operation[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif operation[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
