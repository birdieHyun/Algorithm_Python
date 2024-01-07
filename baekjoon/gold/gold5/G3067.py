T = int(input())
for _ in range(T):
    N = int(input())
    coins = [0] + list(map(int, input().split()))
    target = int(input())

    dp = [0 for _ in range(target + 1)]

    for coin in coins:
        if coin > target:
            continue
        dp[coin] += 1
        for i in range(coin + 1, target + 1):
            dp[i] += dp[i - coin]

    print(dp[target])