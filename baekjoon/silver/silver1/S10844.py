# 길이가 N 인 쉬운 계단 수를 구하자
# 0으로 시작하는 수는 없다.

# N = 1 : 1, 2, 3, 4, 5, 6, 7, 8, 9                                                9개
# N = 2 : 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98       17개
# N = 3 : 121, 123, 212, 232,

# dp[N][L] = 길이가 N 이고, 끝자리가 L일때의 경우의 수

# dp[N][L] = dp[N - 1][L-1] + dp[N - 1][L + 1]

# dp[2][1] = dp[1][0] + dp[1][2] -> 0 + 1 1개
# dp[2][2] = dp[1][1] + dp[1][3] -> 1 + 1 = 2개

# 여기는 L 이 1 ~ 8 일때만 가능하다.

# L이 0일땐
# dp[N][L] = dp[N][L + 1]
# dp[2][0] = dp[1][1]  = 1개

# L이 9일땐
# dp[N][L] = dp[N][L - 1]
# dp[2][9] = dp[1][8] = 1개

N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]
for i in range(1, 10):
    dp[1][i] = 1


for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

answer = 0

for i in range(10):
    answer += dp[N][i]

print(answer % 1000000000)
