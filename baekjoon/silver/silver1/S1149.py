houses = int(input())

house_list = [list(map(int, input().split())) for _ in range(houses)]

for i in range(1, houses):
    house_list[i][0] = house_list[i][0] + min(house_list[i - 1][1], house_list[i - 1][2])
    house_list[i][1] = house_list[i][1] + min(house_list[i - 1][0], house_list[i - 1][2])
    house_list[i][2] = house_list[i][2] + min(house_list[i - 1][0], house_list[i - 1][1])

answer = min(house_list[houses - 1][0], house_list[houses - 1][1], house_list[houses - 1][2])
print(answer)
