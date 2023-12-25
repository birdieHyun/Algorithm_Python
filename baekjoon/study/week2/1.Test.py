N = int(input())
warriors = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if warriors[j] > warriors[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
