# dp[i][j] -> i 번째 물건까지 포함했을 때, j 무게 만큼 담았을 때 최대 값

N, K = map(int, input().split())

goods = []

for _ in range(N):
    weight, value = map(int, input().split())
    goods.append((weight, value))

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = goods[i - 1]

    for j in range(1, K + 1):
        # 물건을 안담는게 답일 수 있음
        dp[i][j] = dp[i - 1][j]
        if j >= weight:
            dp[i][j] = max(dp[i][j], dp[i- 1][j - weight] + value)

print(dp[N][K])