def solution(topping):
    answer = 0

    a = {}
    b = {}

    arr = []
    arr2 = []

    for i in topping:
        a[i] = 1
        arr.append(len(a))

    for i in range(len(topping) -1 , -1, -1):
        b[topping[i]] = 1
        arr2.append(len(b))

    arr2.sort(reverse=True)


    for i in range(len(topping) - 1):
        if arr[i] == arr2[i + 1]:
            answer +=1

    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]	))
