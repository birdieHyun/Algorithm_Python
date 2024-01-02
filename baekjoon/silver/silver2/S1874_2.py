from collections import deque

N = int(input())
answer = []
flag = True
stack = deque()

curr_num = 1

for i in range(N):
    required = int(input())

    while curr_num <= required:
        stack.append(curr_num)
        curr_num += 1
        answer.append('+')

    if stack[-1] == required:
        stack.pop()
        answer.append('-')

    else:
        print('NO')
        flag = False
        break

if flag:
    for i in answer:
        print(i)


