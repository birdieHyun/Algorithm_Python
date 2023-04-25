from collections import deque

def solution(s):
    if len(s) == 1:
        return 0

    queue = deque()

    for i in s:
        if len(queue) == 0:
            queue.append(i)
            continue
        if queue[-1] == i:
            queue.pop()
        else:
            queue.append(i)

    if len(queue) == 0:
        return 1
    else:
        return 0

solution("cdcd")