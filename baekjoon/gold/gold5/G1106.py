import sys

input = sys.stdin.readline

C, N = map(int, input().split())
promotions = [list(map(int, input().split())) for _ in range(N)]

dp = [int(10e9)] * (C + 100)
dp[0] = 0

for i in range(1, C + 100):

    for cost, people in promotions:

        dp[i] = min(dp[i], dp[i - people] + cost)

print(min(dp[C:]))
