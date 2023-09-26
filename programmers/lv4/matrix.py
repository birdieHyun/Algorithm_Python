from collections import deque

def solution(rc, operations):
    answer = []
    left_q = deque()
    mid_q = deque()
    right_q = deque()
    for i in range(len(rc)):
        left_q.append(rc[i][0])
        right_q.append(rc[i][-1])

        tmp = deque()
        for j in range(1, len(rc[i]) - 1):
            tmp.append(rc[i][j])

        mid_q.append(tmp)

    # 모두 O(1)로 해결 가능하다.
    for op in operations:
        if op == 'Rotate':
            mid_q[0].appendleft(left_q.popleft())
            right_q.appendleft(mid_q[0].pop())
            mid_q[-1].append(right_q.pop())
            left_q.append(mid_q[-1].popleft())


        # 모두 O(1) 로 해결 가능하다
        elif op == 'ShiftRow':
            left_q.appendleft(left_q.pop())
            right_q.appendleft(right_q.pop())
            mid_q.appendleft(mid_q.pop())

    # 가로 * 세로가 10만이기 때문에 이중포문 괜찮음
    for i in range(len(left_q)):
        tmp = []
        tmp.append(left_q.popleft())

        for j in range(len(mid_q[i])):
            tmp.append(mid_q[i].popleft())

        tmp.append(right_q.popleft())
        answer.append(tmp)

    return answer

# rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# operations = ["Rotate", "ShiftRow"]
# result = [[8, 9, 6], [4, 1, 2], [7, 5, 3]]

rc = list([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],)
operations = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]

print(solution(rc, operations))