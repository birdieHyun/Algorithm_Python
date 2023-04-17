from collections import deque

answer = 0
def find_direction(str, now_direction):
    if now_direction == 0:
        if str == 'D':
            return 3
        else:
            return 2

    if now_direction == 1:
        if str == 'D':
            return 2
        else:
            return 3

    if now_direction == 2:
        if str == 'D':
            return 0
        else:
            return 1

    if now_direction == 3: 
        if str == 'D':
            return 1
        else:
            return 0

board_size = int(input())
apple_count = int(input())

apple_graph = [[0 for _ in range(board_size)]for _ in range(board_size)]
tail_graph = [[False for _ in range(board_size)]for _ in range(board_size)]

for i in range(apple_count):
    y, x = map(int, input().split())
    apple_graph[y][x] = 1

move_direction = []

index = int(input())

for _ in range(index):
    time, direction = input().split()
    move_direction.append((int(time), direction))

queue = deque()

# L 은 왼쪽 D 는 오른쪽
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

flag = True
# 첫 방향은 오른쪽
now_direction = 3
x = 0
y = 0
queue.append((x, y))

# 벽이나 꼬리 만나지 않을 동안
while flag:
    #움직이는 초와 방향에 대한 정보를 가진 리스트를 순회
    for i in move_direction:
        # 몇 초동안 움직일 것인지
        time = i[0]
        # 초 후에 어떤 방향인지 D 혹은 L 인지 확인
        next_direction_str = i[1]

        # 초 동안 움직인다.
        for _ in range(time):
            if flag == False:
                break
            # 방향으로 다음 위치를 확인한다.
            next_x = x + dx[now_direction]
            next_y = y + dy[now_direction]

            # 사과가 없다는데 꼬리를 만나면 , 혹은 벽을 만나면
            if next_x < 0 or next_y < 0 or next_y >= board_size or next_x  >= board_size:
                flag = False
                break
            elif tail_graph[next_y][next_x] == True:
                flag = False
                break
            # 사과가 있으면 꼬리 제거
            elif apple_graph[next_y][next_x] == 1:
                # 사과를 먹은 것으로 표시
                apple_graph[next_y][next_x] = 0
                # 사과 먹었으니 꼬리 제거
                tail_x, tail_y = queue.popleft()
                tail_graph[tail_y][tail_x] = False
                answer += 1

            # 사과가 없고 진행할 수 있다면
            else:
                x = next_x
                y = next_y
                queue.append((x, y))
                # 꼬리 표시
                tail_graph[y][x] = True
                answer += 1


        now_direction = find_direction(next_direction_str, now_direction)


        if flag == False:
            break





print(answer)
