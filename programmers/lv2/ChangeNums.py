def solution(x, y, n):
    answer = 0
    MAX_NUM = int(10e9)

    dp = [MAX_NUM] * (y + 1)
    dp[x] = 0

    for i in range(x, y + 1):

        tmp1, tmp2, tmp3 = MAX_NUM, MAX_NUM, MAX_NUM

        if i % 2 == 0:
            tmp1 = dp[i // 2] + 1
        if i % 3 == 0:
            tmp2 = dp[i // 3] + 1
        if i - n >= x:
            tmp3 = dp[i - n] + 1

        dp[i] = min(dp[i], tmp1, tmp2, tmp3)

    answer = dp[y]
    if answer == MAX_NUM:
        answer = -1
    return answer

print(solution(10, 40, 5))  # 2
