from collections import deque

size = int(input())
list = list(map(int, input().split()))

list.sort()

q = deque(list)

answer = 0

while q:
    max_fear = q.popleft()
    print(max_fear)

    for _ in range(max_fear - 1):
        if len(q) > 0:
            print(q.popleft())
        else:
            break

    print(q)
    answer += 1

print(answer)
