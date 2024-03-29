N = int(input())
towers = list(map(int, input().split()))
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > towers[i]:  # 수신 가능한 상황
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:  # 스택이 비면 레이저를 수신할 탑이 없다.
        answer.append(0)
    stack.append([i, towers[i]])  # 인덱스, 값

print(" ".join(map(str, answer)))
