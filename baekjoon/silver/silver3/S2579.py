stair_count = int(input())
stairs = []
dp = [0] * (stair_count)



for _ in range(stair_count):
    stairs.append(int(input()))

if stair_count <= 2:
    print(sum(stairs))
else:

    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])

    for i in range(3, stair_count):
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i],
                    dp[i - 2] + stairs[i])

    print(dp[-1])
