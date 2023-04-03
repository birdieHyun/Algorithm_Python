def solution(park, routes):
    answer = []
    park_arr = []
    for i in park:
        park_arr.append(list(i))


    # 시작점 구하기
    start = find_start(park).split()
    start_X = int(start[1])
    start_Y = int(start[0])
    direction = {'N': '-1 0', 'S': '1 0', 'E': '0 1', 'W': '0 -1'}

    for i in routes:
        split = i.split(" ")
        moving = direction[split[0]].split()
        movingX = moving[1]
        movingY = moving[0]


        for i in range(0, int(split[1])):
            start_X += int(movingX)
            start_Y += + int(movingY)
            if start_X < 0 or start_X >= len(park[0]) or start_Y < 0 or start_Y >= len(park[0]):
                start_X -= (i + 1) * int(movingX)
                start_Y -= (i + 1) * int(movingY)
                break
            if park_arr[start_Y][start_X] == 'X':
                start_X -= (i + 1) * int(movingX)
                start_Y -= (i + 1) * int(movingY)
                break

    answer.append(start_Y)
    answer.append(start_X)
    return answer


def find_start(park):
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                return str(i) + ' ' + str(j)


# park = ["SOO", "OOO", "OOO"]
# route = ["E 2", "S 2", "W 1"]
# print(solution(park, route))

# park2 = ["SOO","OXX","OOO"]
# route2 =["E 2","S 2","W 1"]
# print(solution(park2,route2))

park3 = ["OSO","OOO","OXO","OOO"]
route3 = ["E 2","S 3","W 1"]
print(solution(park3, route3))