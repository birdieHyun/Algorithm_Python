import math


def find_bounding_rectangle(x, y, r):
    # 왼쪽 변 (l)과 오른쪽 변 (r)의 x좌표
    left = min([x[i] - r[i] for i in range(len(x))])
    right = max([x[i] + r[i] for i in range(len(x))])

    # 아래쪽 변 (b)과 위쪽 변 (t)의 y좌표
    bottom = min([y[i] - r[i] for i in range(len(y))])
    top = max([y[i] + r[i] for i in range(len(y))])

    return left, right, bottom, top


def find_coordinate(v, left, right, bottom, top):
    coordinate = []

    for i in range(0, len(v), 2):
        x = v[i]
        y = v[i + 1]

        new_x = left + x % (right - left)
        new_y = bottom + y % (top - bottom)
        coordinate.append((new_x, new_y))

    return coordinate


def check_point_within_or_on_circle(point, circle_center, radius):
    # 원의 중심 좌표와 반지름
    cx, cy = circle_center
    r = radius

    # 좌표가 원 내부에 있거나 원의 경계 위에 있는지 확인
    return math.sqrt((point[0] - cx) ** 2 + (point[1] - cy) ** 2) <= r


def solution(x, y, r, v):
    answer = 0
    left, right, bottom, top = find_bounding_rectangle(x, y, r)
    coordinate = find_coordinate(v, left, right, top, bottom)

    count = 0

    for i in coordinate:
        flag = False
        for j in range(len(x)):
            next_x, next_y = x[j], y[j]

            if check_point_within_or_on_circle(i, (next_x, next_y), r[j]):
                flag = True
                break
        if flag:
            count += 1

    k = count / (len(v) // 2)

    return int(k * (right - left) * (top - bottom))


x = [5]
y = [5]
r = [5]
v = [92, 83, 14, 45, 66, 37, 28, 9, 10, 81]

print(solution(x, y, r, v))
