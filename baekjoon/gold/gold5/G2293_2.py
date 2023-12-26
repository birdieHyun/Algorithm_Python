n, target = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] * (target + 1)
dp[0] = 1

for coin in coins:
    for i in range(coin, target + 1):
        dp[i] += dp[i - coin]

print(dp[target])
