from collections import deque

def solution(s):
    queue = deque()
    split = list(s)

    for i in split:
        if i == '(':
            queue.append('(')
        else:
            if len(queue) == 0:
                return False
            queue.popleft()
    if len(queue) != 0:
        return False
    return True

s = '()()'

print(solution(s))