from collections import deque

def solution(prices):
    answer = [0] * len(prices)

    q = deque()

    for i in range(len(prices)- 1, -1, -1):

        while q:
            if q[-1][0] >= prices[i]:
                q.pop()
            else:
                break

        if not q:
            answer[i] = len(prices) - i - 1
        else:
            answer[i] = q[-1][1] - i

        q.append([prices[i], i])


    return answer

prices = [1, 2, 3, 2, 3]
answer = [4, 3, 1, 1, 0]

print(solution(prices))