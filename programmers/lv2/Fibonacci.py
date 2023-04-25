def solution(n):

    numbers_list = []
    numbers_list.append(0)
    numbers_list.append(1)

    for i in range(2, n + 1):
        tmp = (numbers_list[i - 1] + numbers_list[i - 2]) % 1234567
        numbers_list.append(tmp)


    return numbers_list[-1]

print(solution(3))