T = int(input())

for _ in range(T):
    stack = []
    tmp = []
    secret = str(input())
    for i in secret:
        if i == '-':
            if stack: #왼쪽 스택에 있을 경우
                stack.pop()
        elif i == '<': # 왼쪽 스택에 있는 문자 오른쪽 스택으로
            if stack:
                tmp.append(stack.pop())
        elif i == '>': # 오른쪽 스택에 있는 문자 왼쪽 스택으로
            if tmp:
                stack.append(tmp.pop())
        else:
            stack.append(i)
    stack.extend(reversed(tmp)) # 오른쪽 스택에 있는 문자들은 뒤집어서
    print(''.join(stack))