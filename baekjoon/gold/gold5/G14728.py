import sys

input = sys.stdin.readline

N, T = map(int, input().split())

tests = []

for _ in range(N):
    tests.append(list(map(int, input().split())))

dp = [[0] * (T + 1) for _ in range(N)]

for i in range(len(tests)):
    time, value = tests[i][0], tests[i][1]

    for j in range(1, T + 1):

        # 선택하지 않은 경우
        dp[i][j] = dp[i - 1][j]

        if j >= time:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - time] + value)

print(dp[-1][-1])

