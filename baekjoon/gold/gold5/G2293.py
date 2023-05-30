type, total = map(int, input().split())

coin_list = [int(input()) for _ in range(type)]
coin_list.sort()

start = coin_list[0]
dp = [0] * (total + 1)
dp[0] = 1

for coin in coin_list:
    for i in range(coin, total + 1):
        tmp = dp[i - coin]
        dp[i] += tmp

print(dp[total])