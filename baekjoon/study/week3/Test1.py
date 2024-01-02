T, W = map(int, input().split())

jadu = []

for _ in range(T):
    jadu.append(int(input()))

dp = [[0] * (W + 1) for _ in range(T + 1)]

for i in range(1, T + 1):

    next = jadu[i - 1]
    # 한 번도 안움직임
    if next == 1:
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]

    for j in range(1, W + 1):

        # 시간 보다 적게 움직여야 함
        if j > i:
            break

        # 자두가 1에서 떨어짐
        if next == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        # 자두가 2에서 떨어짐
        elif next == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        # 못먹음
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])

print(max(dp[-1]))

