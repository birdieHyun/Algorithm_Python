# size = int(input())
# move = list(map(str, input().split()))
# x, y = 1, 1
#
# for i in range(len(move)):
#     move_to = move[i]
#     if move_to == "U":
#         if(x > 1):
#             x -= 1
#     if move_to == "D":
#         if(x < size):
#             x += 1
#     if move_to == "L":
#         if(y > 1):
#             y -= 1
#     if move_to == "R":
#         if(y < size):
#             y += 1
#
# print(x, y)

# 해설
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):

        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우 무시
            if ny < 1 or nx < 1 or ny > n or nx > n:
                continue

            x, y = nx, ny

print(x, y)
