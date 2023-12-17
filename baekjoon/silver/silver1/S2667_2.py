from collections import deque

n = int(input())

maps = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = []


def bfs(node):
    global answer
    count = 1
    q = deque([node])

    while q:
        x, y = q.popleft()
        visited[y][x] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if not visited[ny][nx] and maps[y][x] == maps[ny][nx]:
                count += 1
                visited[ny][nx] = True

                q.append((nx, ny))

    return count


for i in range(n):
    for j in range(n):
        if not visited[i][j] and maps[i][j] == 1:
            count = bfs((j, i))
            answer.append(count)

print(len(answer))
answer.sort()
for i in answer:
    print(i)