test_case = int(input())

def fib(number):
    zero = [1, 0, 1]
    one = [0, 1, 1]
    if number >= 3:
        for i in range(2, number):
            zero.append(zero[i - 1] + zero[i])
            one.append(one[i - 1] + one[i])
    print(zero[number], one[number])

for _ in range(test_case):
    fib(int(input()))

