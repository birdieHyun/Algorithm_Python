import sys

map = []
size = int(input())
for _ in range(size):
    map.append([int(x) for x in sys.stdin.readline().rstrip().split()])


dp = [[[0 for _ in range(size)] for _ in range(size)] for _ in range(3)]

# 가로는 무조건 1
dp[0][0][1] = 1
for i in range(2,size):
    if map[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for i in range(1,size):
    for j in range(1,size):
        if map[i][j] == 0 and map[i][j - 1] == 0 and map[i - 1][j] == 0:
            dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]
            # 대각선 파이프 놓기

        if map[i][j] == 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            # 가로 파이프 놓기

            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]



answer = dp[0][size - 1][size - 1] + dp[1][size - 1][size - 1] + dp[2][size - 1][size - 1]

print(answer)