list = list(map(int, input().split()))

profit = 0
minimum = max(list)

for i in list:
    minimum = min(i, minimum)
    profit = max(profit, i - minimum)

print(profit)
