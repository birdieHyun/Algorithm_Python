from collections import deque

number = int(input())

q = deque()

for i in range(1, number + 1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q.popleft())