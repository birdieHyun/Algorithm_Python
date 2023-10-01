import sys
input = sys.stdin.readline

N = int(input())
tree = []
dp = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    tree.append(tmp)
    dp_tmp = []
    for _ in range(len(tmp)):
        dp_tmp.append(0)
    dp.append(dp_tmp)

dp[0][0] = tree[0][0]
if N != 1:
    dp[1][0] = dp[0][0] + tree[1][0]
    dp[1][1] = dp[0][0] + tree[1][1]

for i in range(2, N):
    for j in range(len(tree[i])):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + tree[i][j]
        elif j == len(tree[i]) - 1:
            dp[i][j] = dp[i - 1][j - 1] + tree[i][j]
        else:
            dp[i][j] = max(dp[i-1][j - 1], dp[i - 1][j]) + tree[i][j]


print(max(dp[N - 1]))