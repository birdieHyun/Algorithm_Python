import sys

input = sys.stdin.readline


def find_distance(direction, distance):
    if direction == 1:
        return distance
    elif direction == 2:
        return width + height + width - distance
    elif direction == 3:
        return width + height + width + height - distance
    else:
        return width + distance


width, height = map(int, input().split())

shops_count = int(input())

shops = []
for i in range(shops_count + 1):
    if i == shops_count:
        direction, distance = map(int, input().split())
    else:
        shops.append(list(map(int, input().split())))

answer = 0
path1 = find_distance(direction, distance)
for dir, dist in shops:
    path2 = find_distance(dir, dist)

    dist1 = abs(path1 - path2)
    dist2 = 2 * width + 2 * height - dist1

    if dist1 < dist2:
        answer += dist1
    else:
        answer += dist2

print(answer)
