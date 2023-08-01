from collections import deque

n, m = map(int, input().split())

board = [0] * 101

visited = [False] * 101

ladder = dict()
snake = dict()

for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

q = deque([1])

while q:
    x = q.popleft()

    if x == 100:
        print(board[x])
        break

    for dice in range(1, 7):
        moved = x + dice

        if moved <= 100 and not visited[moved]:
            if moved in ladder.keys():
                moved = ladder[moved]
            if moved in snake.keys():
                moved = snake[moved]
            if not visited[moved]:
                visited[moved] = True
                board[moved] = board[x] + 1
                q.append(moved)