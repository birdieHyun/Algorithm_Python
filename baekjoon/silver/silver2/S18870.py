n = int(input())
values = list(map(int, input().split()))

maps = [[] for _ in range(n)]
maps_after = [[] for _ in range(n)]

for i in range(n):
    maps[i] = [i, values[i]]

maps.sort(key=lambda x: x[1])
maps_after[0] = [maps[0][0], 0]

i = 1
while i < n:
    if maps[i][1] == maps[i - 1][1]:
        maps_after[i] = [maps[i][0], maps_after[i - 1][1]]
        maps_after[i][1] = maps_after[i - 1][1]
        i += 1
        continue

    maps_after[i] = [maps[i][0], maps_after[i - 1][1] + 1]
    i += 1

maps_after.sort()

for i in maps_after:
    print(i[1], end=' ')
