import sys

input = sys.stdin.readline

N = int(input())
works = []

for _ in range(N):
    works.append(list(map(int, input().split())))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    next, profit = works[i - 1][0], works[i - 1][1]
    dp[i] = max(dp[i], dp[i - 1])

    if i + next - 1 <= N:
        dp[i + next - 1] = max(dp[i + next - 1], dp[i - 1] + profit)

print(dp[-1])
