n, m = map(int, input().split())

water_map = [list(map(int, input().split())) for _ in range(n)]
cloud_map = [[False] * n for _ in range(n)]
print(cloud_map)

# m번 만큼의 이동
for _ in range(m):
    direction, distance = map(int, input().split())
