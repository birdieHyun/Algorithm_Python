def solution(diet):
    answer = 0
    n = len(diet)
    dp = [[0 * 3 for _ in range(3)] for _ in range(n)]

    # 첫 날은 그냥 식사하는 경우임
    dp[0][0] = int(diet[0][0])
    dp[0][1] = int(diet[0][1])
    dp[0][2] = int(diet[0][2])

    # 이틀
    # 오늘이 내일을 결정해주어야 함
    dp[1][0] = min(dp[0][0], dp[0][1], dp[0][2]) + diet[1][0]
    dp[1][1] = min(dp[0][1], dp[0][2]) + diet[1][1]
    dp[1][2] = dp[0][2] + diet[1][2]

    # 오늘 아침 + 어제 아침 점심 저녁
    # 점심은 어제 점심 저녁
    # 저녁은 어제 저녁

    for i in range(2, n):
        dp[i][0] = min(dp[i - 1][0], dp[i -1][1], dp[i - 1][2]) + diet[i][0]
        dp[i][1] = min(dp[i - 1][1], dp[i - 1][2]) + diet[i][1]
        dp[i][2] = dp[i -1][2] + diet[i][2]

    return min(dp[-1])


diet = [[360, 138, 338], [230, 102, 311], [320, 474, 214], [131, 498, 484], [366, 176, 249], [323, 407, 116], [265, 433, 317]]

print(solution(diet))