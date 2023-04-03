from collections import deque

height, width = map(int, input().split())

graph = [[] for _ in range(height)]

for hei in range(height):
    tmp = input()
    int_list = [int(x) for x in tmp]
    graph[hei] = int_list

queue = deque()

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    # 시작은 항상 0,0 이라고 가정
    queue.append([0, 0])

    while queue:
        # 현재 지점의 x, y 좌표 계산
        now_coordinate = queue.popleft()
        now_X = now_coordinate[0]
        now_Y = now_coordinate[1]

        # 상 하 좌 우 탐색
        for i in range(4):
            moved_X = now_X + dx[i]
            moved_Y = now_Y + dy[i]

            # 좌표값이 범위를 넘어간 경우 스킵
            if moved_X < 0 or moved_X >= width or moved_Y < 0 or moved_Y >= height:
                continue

            # 벽을 만난 경우 스킵
            elif graph[moved_Y][moved_X] == 0:
                continue

            # 아직 가보지 않은 길인 경우에만 탐색, 다른 방향을 통해 가본 길이더라도 현재의 길이 더 짧은 경우의 수라면 값을 변경해준다.
            elif graph[moved_Y][moved_X] == 1 or graph[moved_Y][moved_X] > graph[now_Y][now_X] + 1:
                # 움직인 칸수를 변경해준다.
                graph[moved_Y][moved_X] = graph[now_Y][now_X] + 1
                queue.append([moved_X, moved_Y])
                if moved_Y + 1 == height and moved_X + 1== width:
                    return graph[height - 1][width - 1]

print(bfs())
