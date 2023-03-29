from collections import deque

length, width = map(int, input().split())

maze = []

for i in range(length):
    maze.append(list(map(int, input())))

locationY = [-1, 1, 0, 0]
locationX = [0, 0, -1, 1]


def bfs(y, x):
    queue = deque()
    print(y, x)
    queue.append((y, x))

    while queue:
        y ,x = queue.popleft()
        for i in range(4):
            moveY = locationY[i] + y
            moveX = locationX[i] + x

            if moveY < 0 or moveX < 0 or moveY >= length or moveX >= width:
                continue
            if maze[moveY][moveX] == 0:
                continue

            if maze[moveY][moveX] == 1:
                queue.append((moveY, moveX))
                maze[moveY][moveX] = maze[y][x] + 1
    return maze[length - 1][width - 1]


print(bfs(0, 0))
