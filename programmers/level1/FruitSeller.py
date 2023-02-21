def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)

    for i in range(0, len(score), m):
        tmp = score[i:i + m]

        if len(tmp) == m:
            answer += min(tmp) * m

    return answer

score = [1, 2, 3, 1, 2, 3, 1]


print(solution(3,4, score))