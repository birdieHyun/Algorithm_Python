import math

def solution(n, k):
    answer = []

    num_list = [i for i in range(1, n + 1)]

    while n != 0:
        temp = math.factorial(n) // n
        index = k // temp
        k = k % temp
        if k == 0:
            answer.append(num_list.pop(index - 1))
        else:
            answer.append(num_list.pop(index))

    return answer
