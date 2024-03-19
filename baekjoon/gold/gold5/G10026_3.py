from collections import deque

N = int(input())
rgb = [list(input()) for _ in range(N)]

rgb_visited_color_blind = [[False] * N for _ in range(N)]
rgb_visited = [[False] * N for _ in range(N)]

color_blind_answer = 0
not_color_blind_answer = 0

q = deque()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# R      G         B
def color_blind(start):
    q = deque()
    q.append(start)

    if rgb_visited_color_blind[start[1]][start[0]]:
        return 0

    while q:
        now_x, now_y = q.popleft()
        rgb_visited_color_blind[now_y][now_x] = True

        for i in range(4):
            move_x = now_x + dx[i]
            move_y = now_y + dy[i]

            if move_x < 0 or move_y < 0 or move_x >= N or move_y >= N:
                continue
            if rgb_visited_color_blind[move_y][move_x]:
                continue
            if rgb[now_y][now_x] == 'R' or rgb[now_y][now_x] == 'G':
                if rgb[move_y][move_x] == 'R' or rgb[move_y][move_x] == 'G':
                    if not rgb_visited_color_blind[move_y][move_x]:
                        q.append((move_x, move_y))
                        rgb_visited_color_blind[move_y][move_x] = True

            if rgb[now_y][now_x] == 'B' and rgb[move_y][move_x] == 'B':
                if not rgb_visited_color_blind[move_y][move_x]:
                    q.append((move_x, move_y))
                    rgb_visited_color_blind[move_y][move_x] = True

    return 1


# RG   , B
def not_color_blind(start):
    q = deque()
    q.append(start)

    if rgb_visited[start[1]][start[0]]:
        return 0

    while q:
        now_x, now_y = q.popleft()
        rgb_visited[now_y][now_x] = True

        for i in range(4):
            move_x = now_x + dx[i]
            move_y = now_y + dy[i]

            if move_x < 0 or move_y < 0 or move_x >= N or move_y >= N:
                continue
            if rgb_visited[move_y][move_x]:
                continue
            if rgb[now_y][now_x] == rgb[move_y][move_x] and not rgb_visited[move_y][move_x]:
                q.append((move_x, move_y))
                rgb_visited[move_y][move_x] = True

    return 1


for i in range(N):
    for j in range(N):
        color_blind_answer += color_blind((i, j))
        not_color_blind_answer += not_color_blind((i, j))

print(not_color_blind_answer, color_blind_answer)
