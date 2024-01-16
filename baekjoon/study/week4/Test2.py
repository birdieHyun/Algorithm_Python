from collections import deque

N = int(input())
nums = list(map(int, input().split()))

stack = deque()
answer = []

for i in range(N -1, -1, -1):

    while stack and stack[-1] <= nums[i]:
        stack.pop()

    if not stack:
        answer.append(-1)
        stack.append(nums[i])
    else:
        answer.append(stack[-1])
        stack.append(nums[i])

for i in range(N - 1, -1, -1):
    print(answer[i], end=' ')
