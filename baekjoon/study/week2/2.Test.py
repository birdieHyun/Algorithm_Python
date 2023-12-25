from collections import deque

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

time = 0
q = deque()
time_q = deque()
before = deque(trucks)

while before or q:
    time += 1
    if q and before:
        if time_q[0] == time:
            time_q.popleft()
            q.popleft()
        if sum(q) + before[0] <= l:
            q.append(before.popleft())
            time_q.append(time + w)

    elif q:
        if time_q[0] == time:
            time_q.popleft()
            q.popleft()

    else:
        q.append(before.popleft())
        time_q.append(time + w)



print(time)

# 4 2 10
# 7 4 5 6
# 8
#
# 1 100 100
# 10
# 101
#
# 10 100 100
# 10 10 10 10 10 10 10 10 10 10 10
# 110
