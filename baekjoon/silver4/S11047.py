N, total_money = map(int, input().split())

money_list = []
answer = 0
for i in range(N):
    money_list.append(int(input()))


while total_money > 0:
    for i in range(len(money_list) - 1, -1, -1):
        if (total_money - money_list[i] >= 0):
            count = total_money // money_list[i]
            answer += count

            total_money -= count * money_list[i]

print(answer)