from collections import deque

k = int(input())

q = deque()

for _ in range(k):
    num = int(input())

    if num == 0:
        q.pop()
    else:
        q.append(num)

answer = sum(list(q))
print(answer)
