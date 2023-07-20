from collections import deque

test = int(input())

for _ in range(test):
    length, idx = map(int, input().split())
    num_list = list(map(int, input().split()))

    q = deque(num_list)
    count = 1
    while q:
        if idx == 0 and max(q) == q[0]:
            print(count)
            break
        if idx == 0 and max(q) != q[0]:
            idx = len(q) - 1
            q.append(q.popleft())
        elif max(q) == q[0]:
            count += 1
            q.popleft()
            idx -= 1
        else:
            idx -= 1
            q.append(q.popleft())
