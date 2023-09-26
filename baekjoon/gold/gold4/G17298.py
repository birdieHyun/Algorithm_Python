import sys
from collections import deque

input = sys.stdin.readline

nums = map(int, input())
num_list = list(map(int, input().split()))

answer = []

q = deque()

for i in range(len(num_list) - 1, -1, -1):

    while len(q) > 0 and q[-1] <= num_list[i]:
        q.pop()

    if len(q) == 0:
        answer.append(-1)
        q.append(num_list[i])
    else:
        answer.append(q[-1])
        q.append(num_list[i])

for i in range(len(answer) - 1, -1, -1):
    print(answer[i], end=' ')
