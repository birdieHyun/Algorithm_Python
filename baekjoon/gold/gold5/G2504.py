from collections import deque

stack = deque()

bracket = str(input())

answer = ''

stack.append(bracket[0])

if bracket[0] == '(':
    answer += '(2'
else:
    answer += '(3'

for i in range(1, len(bracket)):
    tmp = bracket[i]

    # answer += ')+'
    if tmp == ')' or tmp == ']':
        answer += ')'

    elif tmp == '(':
        answer += '2'
    else:
        answer += '3'

    answer += '*('
    stack.append(tmp)

print(answer)
