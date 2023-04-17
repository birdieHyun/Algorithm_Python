def solution(number, limit, power):
    measure = []
    for i in range(1, number + 1):
        count = 0
        for j in range(1, int(i ** (1 / 2) + 1)):
            if i % j == 0:
                count += 1
                if j ** 2 != i:
                    count += 1
        if count > limit:
            measure.append(power)
        else:
            measure.append(count)

    return sum(measure)


number = 5
limimt = 3
power = 2
print(solution(number, limimt, power))
