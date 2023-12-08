N, K = map(int, input().split())

answer = 0

road = [int(10e9)] * 200001
road[N] = 0

for i in range(N, -1, -1):
    road[i] = min(road[i + 1] + 1, road[i])

for i in range(N, K + 2):
    road[i] = min(min(road[i - 1], road[i + 1]) + 1, road[i])
    if i % 2 == 0:
        road[i] = min(road[i], road[i // 2] + 1)
    road[i - 1]  = min(road[i - 1], road[i] + 1)

answer = road[K]

if K < N:
    answer = N - K

print(answer)
