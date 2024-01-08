import sys

input = sys.stdin.readline


N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

dp = [0] * (N +  1)
dp[0] = nums[0]
dp[1] = nums[0] + nums[1]

for i in range(2, N):
    dp[i] = max(dp[i - 1], nums[i] + nums[i - 1] + dp[i - 3], nums[i] + dp[i - 2])

print(max(dp))