N, M, R = map(int, input().split())

domino = [list(map(int, input().split()))for _ in range(N)]

domino_falled = [[False] * M for _ in range(N)]


for _ in range(R):
    str_y, str_x, direction = map(str, input().split())
    y = int(str_y) - 1
    x = int(str_x) - 1

    up_y, up_x = map(int, input().split())
    up_y -= 1
    up_x -= 1
    to_move = (domino[y][x] - 1)


    # 도미노가 이미 넘어졌으면 공격자 넘어감
    if domino_falled[y][x] == True:
        domino_falled[up_y][up_x] = True
        continue

    domino_falled[y][x] = True

    while 0 < to_move <= N or 0 < to_move <= M:
        if direction == 'E':
            x += 1
            if x >= M or domino_falled[y][x] == True:
                break
            to_move += (domino[y][x] - 1)
            domino_falled[y][x] = False



        elif direction == 'W':
            x -= 1
            if x < 0 or domino_falled[y][x] == True:
                break
            to_move += (domino[y][x] - 1)
            domino_falled[y][x] = False



        elif direction == 'S':
            y += 1
            if y >= N or domino_falled[y][x] == True:
                break
            to_move += (domino[y][x] - 1)
            domino_falled[y][x] = False


        elif direction == 'N':
            y -= 1

            if y > 0 or domino_falled[y][x] == True:
                break
            to_move += (domino[y][x] - 1)
            domino_falled[y][x] = False

    domino_falled[up_y][up_x] = True



print(domino_falled)
