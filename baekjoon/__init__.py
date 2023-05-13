N = 17
L = 17

points = {(3,4), (4,12), (10,16), (12, 13), (2, 11), (7,10), (7,12), (10,11), (10,8), (12,7), (15,13), (14,15), (6,14), (10,13), (13,16), (14,14), (4,4)}

dp = [[0]*(L+1) for _ in range(L+1)]
for point in points:
    dp[point[0]][point[1]] = 1

for i in range(1, L+1):
    for j in range(1, L+1):
        dp[i][j] += max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
