import sys

input = sys.stdin.readline

N, K = map(int, input().split())

classes = []

for _ in range(K):
    classes.append(list(map(int, input().split())))

dp = [[0] * (N + 1)for _ in range(K)]

for i in range(len(classes)):

    value, time = classes[i][0], classes[i][1]

    for j in range(1, N + 1):
        # 수강하지 않은 경우
        dp[i][j] = dp[i - 1][j]

        if j >= time:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - time] + value)

print(dp[-1][-1])