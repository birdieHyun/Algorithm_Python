test_case = int(input())

for _ in range(test_case):
    coin_type = int(input())
    coin_list = list(map(int,input().split()))
    total = int(input())

    d = [0] * (total + 1)
    d[0] = 1

    for coin in coin_list:
        for i in range(1, total + 1):
            if i >= coin:
                d[i] += d[i - coin]

    print(d[total])

