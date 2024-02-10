n = int(input())
money = [500, 100, 50, 10, 5, 1]

rest = 1000 - n
answer = 0

for i in range(6):

    while True:
        if rest - money[i] >= 0:
            answer += 1
            rest -= money[i]

        else:
            break

print(answer)
