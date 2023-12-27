# 물품의 수 N 무게 K
N, K = map(int, input().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]
goods = []

for _ in range(N):
    weight, value = map(int, input().split())
    goods.append((weight, value))

for i in range(1, N + 1):
    weight, value = goods[i - 1]

    for j in range(1, K + 1):
        # 물건을 넣지 않은 경우
        dp[i][j] = dp[i - 1][j]

        if j >= weight:
            # 물건을 넣지 않은 경우와, 이전 것에서 물건을 추가한 경우 중 최대값
            dp[i][j] = max(dp[i][j], dp[i - 1][j - weight] + value)

print(dp[i][j])