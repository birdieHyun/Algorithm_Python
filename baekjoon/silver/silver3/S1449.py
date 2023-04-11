a, b = map(int, input().split())

water_list = list(map(int, input().split()))

water_list.sort()

start = water_list[0]
answer = 1

for i in water_list:
    if i in range(start, start + b):
        continue
    else:
        start = i
        answer += 1

print(answer)