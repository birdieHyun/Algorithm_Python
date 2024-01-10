n = int(input())
array = list(map(int, input().split()))

dp = [0] * n
dp[1] = array[1]

dp[0] = array[0]
for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + array[i])
        else:
            dp[i] = max(dp[i], array[i])

print(max(dp))
