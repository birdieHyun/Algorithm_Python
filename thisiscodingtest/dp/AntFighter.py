food = int(input())
food_count = list(map(int, input().split()))

d = [0] * 100

d[0] = food_count[0]

d[1] = max(food_count[0], food_count[1])

for i in range(2, food):
    d[i] = max(d[i - 1], d[i - 2] + food_count[i])

print(d[food - 1])

