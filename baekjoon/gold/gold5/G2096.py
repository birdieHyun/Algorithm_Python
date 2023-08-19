# 최솟값은 index 1
def min_bfs(column, row):
    min_tmp = int(1e9)
    now_column = column - 1

    for i in range(3):
        now_row = row + row_move[i]
        # 0, 1, 2 벗어나면 스킵
        if now_row == -1 or now_row == 3:
            continue

        tmp = num_list[column][row][0] + num_list[now_column][now_row][1]

        if tmp < min_tmp:
            min_tmp = tmp


    return min_tmp


# 최댓값은 index 2
def max_bfs(column, row):
    max_tmp = 0
    now_column = column - 1

    for i in range(3):
        now_row = row + row_move[i]
        # 0, 1, 2 벗어나면 스킵
        if now_row == -1 or now_row == 3:
            continue
        tmp = num_list[column][row][0] + num_list[now_column][now_row][2]

        if tmp > max_tmp:
            max_tmp = tmp

    return max_tmp

N = int(input())

max_num = 0
min_num = int(1e9)

row_move = [-1, 0, 1]

num_list = []

# 3차원 배열 생성 -> 자신의값, 최솟값, 최댓값
for _ in range(N):
    a, b, c = map(int, input().split())
    tmp = []
    tmp.append([a, min_num, max_num])
    tmp.append([b, min_num, max_num])
    tmp.append([c, min_num, max_num])
    num_list.append(tmp)

# 첫 줄은 최댓값, 최솟값 자신으로 변경
num_list[0][0][1], num_list[0][0][2] = num_list[0][0][0], num_list[0][0][0]
num_list[0][1][1], num_list[0][1][2] = num_list[0][1][0], num_list[0][1][0]
num_list[0][2][1], num_list[0][2][2] = num_list[0][2][0], num_list[0][2][0]

for column in range(1, N):
    for row in range(3):
        now_min = min_bfs(column, row)
        now_max = max_bfs(column, row)

        num_list[column][row][1] = now_min
        num_list[column][row][2] = now_max

answer_max = max(num_list[N - 1][0][2], num_list[N - 1][1][2], num_list[N - 1][2][2])
answer_min = min(num_list[N - 1][0][1], num_list[N - 1][1][1], num_list[N - 1][2][1])

print(answer_max, answer_min)

############

import sys

input = sys.stdin.readline

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_tmp[j] = a + max(max_dp[j], max_dp[j + 1])
            min_tmp[j] = a + min(min_dp[j], min_dp[j + 1])
        elif j == 1:
            max_tmp[j] = b + max(max_dp[j - 1], max_dp[j], max_dp[j + 1])
            min_tmp[j] = b + min(min_dp[j - 1], min_dp[j], min_dp[j + 1])
        else:
            max_tmp[j] = c + max(max_dp[j], max_dp[j - 1])
            min_tmp[j] = c + min(min_dp[j], min_dp[j - 1])

    for j in range(3):
        max_dp[j] = max_tmp[j]
        min_dp[j] = min_tmp[j]

print(max(max_dp), min(min_dp))