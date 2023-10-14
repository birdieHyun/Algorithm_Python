# N 부터 0 까지 -1 씩 하면서 dp 채워줌
# i 가 짝수면, dp[i] = min(dp[i / 2], dp[i-1] + 1)
# i 가 홀수면, dp[i] = min(dp[i / 2] + 1, dp[i-1] + 1)

N, K = map(int, input().split())

dp = [0] * (K + 1)


tmp = 0
for i in range(N, 0, -1):
    dp[i] = tmp
    tmp += 1

for i in range(N + 1, K + 1):
    # 짝수면
    if i % 2 == 0:
        index = int(i / 2)
        dp[i] = min(dp[i - 1] + 1, dp[index])

    # 홀수면
    else:
        index = int(i / 2)
        dp[i] = min(dp[i - 1] + 1, dp[index] + 1)
