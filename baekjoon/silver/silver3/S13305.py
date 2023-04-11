cities = map(int, input())

length = list(map(int, input().split()))

price = list(map(int, input().split()))

current_oil = 0
expense = 0

total_length=sum(length)

current_oil = length[0]
expense += length[0] *price[0]

for i in range(cities):
    