import sys

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = [list(map(int, input().split())) for _ in range(N)]

sums = [list(map(int, input().split())) for _ in range(M)]

dp = [[0] * N for _ in range(N)]

dp[0][0] = numbers[0][0]

for i in range(1, N):
    dp[0][i] = dp[0][i - 1] + numbers[0][i]

for i in range(1, N):
    for j in range(N):
        if j == 0:
            dp[i][j] = dp[i - 1][N - 1] + numbers[i][j]
            continue
        dp[i][j] = dp[i][j - 1] + numbers[i][j]

for i in sums:
    x1, y1, x2, y2 = i
    to_num = dp[y2- 1][x2 - 1]
    from_num = dp[y1 - 1][x1 - 1]
    print(to_num - from_num)