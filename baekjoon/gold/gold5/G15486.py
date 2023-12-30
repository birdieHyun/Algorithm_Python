import sys

input = sys.stdin.readline

N = int(input())
works = []

for _ in range(N):
    works.append(list(map(int, input().split())))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = max(dp[i], dp[i - 1])
    time, profit = works[i - 1][0], works[i - 1][1]

    if i + time - 1 <= N:
        dp[i + time - 1] = max(dp[i + time - 1], dp[i - 1] + profit)

print(max(dp))