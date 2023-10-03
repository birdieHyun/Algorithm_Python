from collections import deque

q = deque()

N = int(input())
top = list(map(int, input().split()))

answer = [0] * N

for i in range(N - 1, -1, -1):
    if len(q) > 0:


    else:
        q.append((top[i], i))

print(q)
print(q.pop())

print(answer)