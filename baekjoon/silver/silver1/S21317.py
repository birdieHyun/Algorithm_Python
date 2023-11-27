# 1 2
# 2 3
# 4 5
# 6 7

N = int(input())
jum_list = [list(map(int, input().split())) for _ in range(N - 1)]
k = int(input())

dp = [0] * (N + 1)

dp[2] = jum_list[0][0]
dp[3] = min(dp[1] + jum_list[1][1], dp[2] + jum_list[1][0])

print(dp)