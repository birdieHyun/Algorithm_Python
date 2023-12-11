from collections import deque


def solution(maps):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque()
    q.append((0, 0))
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]

    while q:

        x, y = q.popleft()
        visited[y][x] = True

        for i in range(4):
            move_x = x + dx[i]
            move_y = y + dy[i]

            # 칸을 벗어 나는 경우
            if move_x < 0 or move_y < 0 or move_x >= len(maps[0]) or move_y >= len(maps):
                continue

            # 벽 인경우
            if maps[move_y][move_x] == 0:
                continue

            if not visited[move_y][move_x]:
                visited[move_y][move_x] = True
                q.append((move_x, move_y))

                if maps[move_y][move_x] == 1:
                    maps[move_y][move_x] = maps[y][x] + 1
                else:
                    maps[move_y][move_x] = min(maps[y][x] + 1, maps[move_y][move_x])

    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

print(solution(maps))