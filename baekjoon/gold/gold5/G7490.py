T = int(input())


def select_operator(now, answer):
    if now == n + 1:
        calculate(answer)
        return

    select_operator(now + 1, answer + ' ' + str(now))
    select_operator(now + 1, answer + '+' + str(now))
    select_operator(now + 1, answer + '-' + str(now))


def calculate(answer):
    tmp = answer.replace(' ', '')
    if eval(tmp) == 0:
        print(answer)


for _ in range(T):
    n = int(input())
    select_operator(2, '1')
    print()
