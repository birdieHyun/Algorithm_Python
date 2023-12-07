from collections import deque

width, height = map(int, input().split())

battle = []
visited = []

for _ in range(height):
    visited.append([False] * width)
    battle.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start):
    count = 0
    queue = deque([(start[0], start[1])])

    while queue:
        now_x, now_y = queue.popleft()
        if visited[now_y][now_x] == False:
            count += 1
        visited[now_y][now_x] = True

        for i in range(4):
            move_x = now_x + dx[i]
            move_y = now_y + dy[i]

            if move_x < 0 or move_y < 0 or move_y >= height or move_x >= width:
                continue
            if battle[now_y][now_x] != battle[move_y][move_x]:
                continue
            if visited[move_y][move_x] == False:
                visited[move_y][move_x] = True
                queue.append((move_x, move_y))
                count += 1
    return count * count

white = 0
black = 0

for i in range(height):
    for j in range(width):
        power = bfs([j, i])
        if battle[i][j] == 'B':
            black += power
        else:
            white += power

print(white, black)
